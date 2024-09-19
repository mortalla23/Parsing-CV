import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue'; // Chemin correct pour HomePage.vue

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
