import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import PasswordReset from './views/PasswordReset.vue';
import Standings from './views/Standings.vue';
import Schedule from './views/Schedule.vue';
import Teams from './views/Teams.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/reset',
      name: 'reset',
      component: PasswordReset,
    },
    {
      path: '/standings',
      name: 'standings',
      component: Standings,
    },
    {
      path: '/schedule',
      name: 'schedule',
      component: Schedule,
    },
    {
      path: '/teams',
      name: 'teams',
      component: Teams,
    },
  ],
});
