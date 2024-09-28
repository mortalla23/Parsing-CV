<template>
    <div class="parser-page">
      <h1>Page de Parsing des CV</h1>
      <p>
        Veuillez télécharger le CV du candidat et entrer la description du poste pour commencer l'analyse.
      </p>
  
      <!-- Champ pour télécharger le CV -->
      <div class="input-group">
        <label for="cv-upload">Télécharger CV :</label>
        <input type="file" id="cv-upload" @change="handleCVUpload" />
      </div>
  
      <!-- Champ pour la description du poste -->
      <div class="input-group">
        <label for="job-desc">Description du poste :</label>
        <textarea id="job-desc" v-model="jobDescription" placeholder="Collez la description du poste ici..."></textarea>
      </div>
  
      <!-- Boutons pour télécharger et visualiser -->
      <div class="buttons">
        <button @click="uploadCV" class="upload-button">Télécharger</button>
        <button @click="visualizeResults" class="visualize-button">Visualiser</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ParserPage',
    data() {
      return {
        jobDescription: '', // Contient la description du poste
        cvFile: null,       // Contient le fichier CV téléchargé
      };
      // modification a prévoir ( le fait de telecharger plusieurs cv a la fois)
    },
    methods: {
      handleCVUpload(event) {
        this.cvFile = event.target.files[0]; // Récupère le fichier téléchargé
      },

      uploadCV() {
        if (this.cvFile) {
          // Logique pour télécharger le CV
          alert('CV téléchargé : ' + this.cvFile.name);
        } else {
          alert('Veuillez télécharger un CV');
        }
        
      },
      visualizeResults() {
        if (this.cvFile && this.jobDescription) {
          // Logique pour visualiser les résultats de parsing
          // requette post pour l'envoie au serveur python ( backend/serveur-python.py ) par la route post http://localhost:5000/upload
          

          alert('Analyse lancée avec succès');
        } else {
          alert('Veuillez télécharger un CV et entrer la description du poste');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .parser-page {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
    background-color: #f0f9f0;
    color: #2f4f2f;
  }
  
  h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
  }
  
  .input-group {
    margin-bottom: 1.5rem;
    width: 100%;
    max-width: 500px;
  }
  
  label {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
    display: block;
  }
  
  input,
  textarea {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  textarea {
    height: 150px;
  }
  
  .buttons {
    display: flex;
    gap: 20px;
  }
  
  .upload-button,
  .visualize-button {
    background-color: #32a852;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.2rem;
  }
  
  .upload-button:hover,
  .visualize-button:hover {
    background-color: #28a745;
  }
  </style>
  