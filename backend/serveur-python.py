import flask
import openai
import os
import time
from flask import Flask, request, jsonify

# Clés et identifiants OpenAI
api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
assistant_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
vector_store_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Configuration de l'application Flask
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialisation du client OpenAI
client = openai.OpenAI(api_key=api_key)

# Fonction pour récupérer la description du poste
def description_du_post(post_desc):
    return post_desc

# Création d'un thread si nécessaire
def creer_thread_si_besoin(session_state):
    if not session_state.get('thread_id'):
        chat = client.beta.threads.create(messages=session_state.get('messages', []))
        session_state['thread_id'] = chat.id

# Route pour le téléchargement des CV et traitement
@app.route('/upload', methods=['POST'])
def upload_file():
    # Vérifier que le fichier et la description du poste sont présents dans la requête
    if 'cv' not in request.files or 'jobDescription' not in request.form:
        return jsonify({"error": "CV et description du poste requis"}), 400
    
    # Récupérer le fichier CV et la description du poste
    file = request.files['cv']
    job_desc = request.form['jobDescription']

    if file.filename == '':
        return jsonify({"error": "Aucun fichier sélectionné"}), 400

    # Sauvegarder le fichier CV
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Ajouter le fichier au vector store (fonction file_search)
    try:
        file_stream = open(file_path, "rb")  # Ouvrir le fichier pour le traitement
        file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id, files=[file_stream]
        )
        
        # Vérifier que les fichiers ont bien été ajoutés au vector store
        if file_batch.status != 'completed':
            return jsonify({"error": "Échec de l'ajout du fichier au vector store"}), 500
    except Exception as e:
        return jsonify({"error": f"Erreur lors de l'upload du fichier : {str(e)}"}), 500

    # Utilisation de l'assistant OpenAI pour analyser le CV et la description du poste
    session_state = {}  # Gestion de l'état fictif
    creer_thread_si_besoin(session_state)

    # Envoyer une requête à l'assistant avec l'instruction pour rechercher le fichier CV
    assistant_instruction = f"""
    Tu dois analyser le CV uploadé dans le vector store et comparer sa cohérence avec la description du poste suivante :
    {job_desc}.
    Le fichier CV est accessible via le vector store grâce à la fonctionnalité file_search.
    """

    client.beta.threads.messages.create(
        thread_id=session_state['thread_id'],
        role="user",
        content=assistant_instruction
    )

    # Lancer l'analyse avec l'assistant en utilisant le vector store et file_search
    run = client.beta.threads.runs.create(
        thread_id=session_state['thread_id'],
        assistant_id=assistant_id
    )

    # Attendre la complétion de l'analyse
    while run.status != "completed":
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(
            thread_id=session_state['thread_id'],
            run_id=run.id
        )

    # Récupérer et traiter les messages du thread
    messages_response = client.beta.threads.messages.list(thread_id=session_state['thread_id'])
    messages = messages_response.data
    latest_message = messages[0]

    # Extraire le texte de la réponse
    response_text = ""
    for content_item in latest_message.content:
        if content_item.type == 'text':
            response_text += content_item.text.value

    # Envoyer la réponse sous forme de JSON au frontend
    return jsonify({"response": response_text})

# Exécution de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
