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
  import axios from 'axios';
  
  export default {
    name: 'ParserPage',
    data() {
      return {
        jobDescription: '', // Contient la description du poste
        cvFiles: [],        // Contient les fichiers CV téléchargés
      };
    },
    methods: {
      // Gère le téléchargement de plusieurs fichiers CV
      handleCVUpload(event) {
        this.cvFiles = Array.from(event.target.files); // Récupère tous les fichiers téléchargés
      },
  
      // Télécharge les fichiers CV sur le serveur
      uploadCV() {
        if (this.cvFiles.length > 0) {
          this.cvFiles.forEach(file => {
            const formData = new FormData();
            formData.append('cv', file);  // Utilise 'cv' si c'est ce que ton backend Flask attend
            formData.append('jobDescription', this.jobDescription);  // Assure-toi que cette clé est attendue comme telle par le backend

            axios.post('http://localhost:5000/upload', formData)
              .then(() => {
                alert(`CV téléchargé avec succès : ${file.name}`);
              })
              .catch(error => {
                alert(`Erreur lors du téléchargement du CV : ${error.response?.data?.message || error.message}`);
              });
          });
        } else {
          alert('Veuillez sélectionner au moins un CV');
        }
      },

  
      // Envoie les fichiers CV et la description du poste pour analyse
      visualizeResults() {
        if (this.cvFiles.length > 0 && this.jobDescription) {
          const formData = new FormData();
          this.cvFiles.forEach(file => {
            formData.append('files', file);
          });
          formData.append('description', this.jobDescription);
  
          axios.post('http://localhost:5000/analyze', formData)
            .then(response => {
              alert('Analyse complétée avec succès: ' + response.data.result);
            })
            .catch(error => {
              alert('Erreur lors de analyse des données: ' + error.response?.data?.message || error.message);
            });
        } else {
          alert('Veuillez télécharger un ou plusieurs CV et entrer la description du poste');
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
  