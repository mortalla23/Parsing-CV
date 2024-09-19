<template>
  <nav class="navbar">
    <!-- Logo -->
    <div class="navbar-logo">
      <router-link to="/">
        <img src="path-to-your-logo.png" alt="Logo" />
      </router-link>
      <h1>CV <span>Matcher</span></h1>
    </div>

    <!-- Liens de navigation -->
    <ul class="navbar-links">
      <li><router-link to="/about">À propos de nous</router-link></li>

      <li class="dropdown">
        <a href="#">Logiciel</a>
        <!-- Dropdown Menu -->
        <div class="dropdown-content">
          <router-link to="/analyse-cv">Analyse automatique des CVs</router-link>
          <a href="#">Matching intelligent</a>
        </div>
      </li>
      <li><a href="#">Partenaires</a></li>
    </ul>

    <!-- Bouton Contact -->
    <button class="contact-button">CONTACT</button>
  </nav>
</template>

<script>
export default {
  name: 'NavbarSection',
};
</script>

<style scoped>
/* Ajout de styles pour éviter les marges supplémentaires */
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin: 0; /* Suppression des marges */
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000; /* S'assurer que la navbar reste au-dessus */
}

.navbar-logo {
  display: flex;
  align-items: center;
}

.navbar-logo img {
  height: 50px;
  margin-right: 10px;
}

.navbar-logo h1 {
  font-size: 1.5rem;
  color: #333;
  margin: 0;
}

.navbar-logo span {
  font-weight: bold;
  color: #333;
}

.navbar-links {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.navbar-links li {
  margin: 0 15px;
  position: relative;
}

.navbar-links a {
  text-decoration: none;
  color: #333;
  font-size: 1rem;
  padding: 10px;
}

.navbar-links .dropdown {
  position: relative;
}

.navbar-links .dropdown:hover .dropdown-content {
  display: block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  z-index: 1;
  top: 100%; /* Assure que le menu est juste en dessous */
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  border-radius: 5px;
  padding: 0;
}

.dropdown-content a {
  display: block;
  padding: 12px 30px;
  color: #333;
  text-decoration: none;
  white-space: nowrap;
}

.dropdown-content a:hover {
  background-color: #f9f9f9;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.contact-button {
  background-color: #ff4242;
  color: white;
  padding: 7px 18px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  position: relative;
  left: -25px; /* Déplace le bouton vers la gauche de 10 pixels */
}

.contact-button:hover {
  background-color: #ff2020;
}
</style>

