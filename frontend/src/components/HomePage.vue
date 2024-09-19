<template>
  <div class="home">
     <!-- Section du projet de parsing -->
     <header>
      <h1>CV Matcher</h1>
    </header>
    <!-- Section Notre mission -->
    <section class="mission-section">
      <div class="text-content">
        <h2>Notre mission</h2>
        <p>
          Le but principal de ce projet est de <strong>moderniser et de simplifier </strong>le travail des Ressources Humaines (RH)
          en automatisant <strong>le tri et la sélection des CV</strong>. Grâce à une application web intuitive, 
          le système analyse les documents soumis, tels que les CV et les descriptions de postes, 
          pour identifier et classer automatiquement <strong>les CV les plus pertinents</strong> par rapport aux exigences du poste. 
          
        </p>
        <p>
          Ce projet vise à rendre le processus de recrutement plus efficace en fournissant aux RH 
          un <strong>outil performant et rapide pour le traitement des candidatures</strong>.
        </p>
        <router-link to="/about">
          <button class="cta-button">Pourquoi nous choisir ?</button>
        </router-link>
      </div>

      <div class="graphic-content">
    <div class="rotating-circle">
      <div class="graphic-section cv-upload">
        <span class="icon">📄</span>
        <span class="text">Télécharger CV</span>
      </div>
      <div class="graphic-section cv-analysis">
        <span class="icon">🔍</span>
        <span class="text">Analyse Automatique</span>
      </div>
      <div class="graphic-section matching">
        <span class="icon">💼</span>
        <span class="text">Matching Intelligent</span>
      </div>
      <div class="graphic-section results">
        <span class="icon">📊</span>
        <span class="text">Résultats</span>
      </div>
    </div>
  </div>
    </section>

    
    
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
  padding: 50px;
  background-color: #f9f9f9;
}

header {
  text-align: center;
  margin-bottom: 50px;
}

h1 {
  font-size: 2.5rem;
  color: #222;
}

p {
  font-size: 1.2rem;
  color: #555;
  margin-bottom: 1.5rem;
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

.mission-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin-top: 50px;
}

.text-content {
  flex: 1;
  padding-right: 50px;
}

h2 {
  font-size: 2.5rem;
  color: #222;
}

.cta-button {
  background-color: #28a745;
  color: white;
  padding: 12px 24px;
  font-size: 1.1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.cta-button:hover {
  background-color: #28a745;
}

.graphic-content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.graphic-circle {
  position: relative;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background-color: #fff;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: center;
  align-items: center;
}

.graphic-section {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 100px;
  text-align: center;
}

.insight {
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  color: #6c2e91;
}

.marque {
  bottom: 10px;
  left: 20px;
  color: #fca531;
}

.sourcing {
  bottom: 10px;
  right: 20px;
  color: #f0b529;
}

.icon {
  font-size: 2rem;
  margin-bottom: 10px;
}

.text {
  font-size: 1rem;
  font-weight: bold;
}


.graphic-content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
  background-color: #f9f9f9;
}

.rotating-circle {
  position: relative;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background-color: #fff;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  animation: rotate 10s infinite linear;
}

.graphic-section {
  position: absolute;
  width: 100px;
  height: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  border-radius: 50%;
  background-color: #f0f9f0;
  color: #333;
  font-weight: bold;
}

.cv-upload {
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
}

.cv-analysis {
  bottom: 10px;
  left: 10px;
}

.matching {
  bottom: 10px;
  right: 10px;
}

.results {
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
  animation-delay: 0.6s;
}
/* Animation de rotation */
@keyframes rotate {
  50% {
    transform: rotate(5deg);
  }
  50% {
    transform: rotate(5deg);
  }
}


.icon {
  font-size: 2rem;
  margin-bottom: 10px;
}

</style>
