<template>
    <div class="analyse-cv-page">
      <h1>Analyse Automatique des CVs</h1>
      <p>
        Cette page vous permet de démarrer l'analyse automatique des CVs. Utilisez le bouton ci-dessous pour commencer le processus.
      </p>
      <button @click="goToParsingPage" class="parser-button">
        Analyser
      </button>
    </div>
  </template>
  
  <script>
  export default {
    name: "AnalyseCV",
    methods: {
      goToParsingPage() {
        this.$router.push("/parsing"); // Redirige vers la page de parsing
      },
    },
  };
  </script>
  
  <style scoped>
  .analyse-cv-page {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 50px;
  }
  
  h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
  }
  
  .parser-button {
    background-color: #32a852;
    color: white;
    padding: 10px 20px;
    font-size: 1.2rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  }
  
  .parser-button:hover {
    background-color: #28a745;
  }
  </style>
  