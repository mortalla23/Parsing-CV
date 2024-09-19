import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import ParserPage from './components/ParserPage.vue'; // Importe la page de parsing
import AnalyseCV from './components/AnalyseCV.vue'; 
import AboutUs from './components/AboutUs.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/parsing',
    name: 'ParserPage',
    component: ParserPage, // Ajoute la route pour ParserPage
  },
  {
    path: '/about',
    name: 'AboutUs',
    component: AboutUs, // Ajouter la route pour la page À propos de nous
  },
  {
    path: '/analyse-cv',
    name: 'AnalyseCV',
    component: AnalyseCV,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
