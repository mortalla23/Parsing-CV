<template>
    <div class="home">
      <header>
        <h1>Projet de Parsing de CV</h1>
        <p>
          Cette application aide les Ressources Humaines à trier automatiquement les CV
          en fonction de la description du poste. Utilisez le bouton ci-dessous pour 
          commencer le processus de parsing des CV.
        </p>
      </header>
      <button @click="goToParsingPage" class="parser-button">
        Parser
      </button>
    </div>
  </template>
  
  <script>
  export default {
    name: "HomePage",
    methods: {
      goToParsingPage() {
        this.$router.push("/parsing");
      },
    },
  };
  </script>
  
  <style scoped>
  .home {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f9f0;
    color: #2f4f2f;
  }
  
  header {
    text-align: center;
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
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.2rem;
  }
  
  .parser-button:hover {
    background-color: #28a745;
  }
  </style>
  