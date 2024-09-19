import Vue from 'vue';
import App from './App.vue';
import router from './router'; // Importer le routeur

Vue.config.productionTip = false;

new Vue({
  router, // Utiliser le routeur dans l'application
  render: h => h(App),
}).$mount('#app');
