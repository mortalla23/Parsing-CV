import { createApp } from 'vue'; // Import de createApp pour Vue 3
import App from './App.vue';
import router from './router'; // Import du routeur

createApp(App)
  .use(router) // Utilisation du routeur
  .mount('#app'); // Montre l'application dans #app
