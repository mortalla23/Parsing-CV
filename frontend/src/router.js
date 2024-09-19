import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from '../views/HomePage.vue';

// import Parser from '../views/Parser.vue'; // À créer si nécessaire

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
//   {
//     path: '/parser',
//     name: 'Parser',
//     component: Parser,
//   },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
