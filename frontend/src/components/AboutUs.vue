<template>
    <div class="about-us-container">
      <section class="intro-section">
        <h1>À propos de nous</h1>
        <p>
          Bienvenue sur notre plateforme innovante dédiée à l'automatisation du traitement des CVs. 
          Nous simplifions et modernisons le processus de recrutement pour les entreprises de toutes tailles.
        </p>
      </section>
  
      <section class="mission-section">
        <h2>Notre Mission</h2>
        <p>
          Notre mission est d'aider les entreprises à optimiser leurs processus de recrutement en automatisant le tri et l'analyse des CVs. 
          Grâce à nos technologies avancées, nous permettons aux équipes RH de se concentrer sur l'essentiel : la sélection des meilleurs talents.
        </p>
      </section>
  
      <section class="values-section">
        <h2>Nos Valeurs</h2>
        <div class="values-list">
          <div class="value-item">
            <h3>Innovation</h3>
            <p>
              Nous utilisons les dernières technologies pour offrir une solution de pointe, toujours à la hauteur des besoins des entreprises modernes.
            </p>
          </div>
          <div class="value-item">
            <h3>Efficacité</h3>
            <p>
              Notre plateforme permet de réduire le temps de traitement des candidatures, tout en améliorant la précision du tri et du matching.
            </p>
          </div>
          <div class="value-item">
            <h3>Fiabilité</h3>
            <p>
              En tant que partenaire de confiance, nous garantissons une expérience utilisateur fluide et des résultats fiables pour chaque étape du recrutement.
            </p>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutUs',
  };
  </script>
  
  <style scoped>
  .about-us-container {
    padding: 0 20px;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .intro-section {
    text-align: center;
    padding: 50px 0;
    background-color: #f0f9f0;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  }
  
  .intro-section h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: #2f4f2f;
  }
  
  .intro-section p {
    font-size: 1.2rem;
    color: #555;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .mission-section, .values-section {
    padding: 40px 0;
    text-align: center;
  }
  
  .mission-section h2, .values-section h2 {
    font-size: 2rem;
    margin-bottom: 20px;
    color: #333;
  }
  
  .mission-section p, .values-section p {
    font-size: 1.1rem;
    color: #555;
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.6;
  }
  
  .values-list {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 20px;
  }
  
  .value-item {
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    width: 300px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .value-item h3 {
    font-size: 1.5rem;
    color: #2f4f2f;
    margin-bottom: 10px;
  }
  
  .value-item p {
    font-size: 1rem;
    color: #555;
  }
  </style>
  