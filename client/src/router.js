import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import PasswordReset from './views/PasswordReset.vue';
import Standings from './views/Standings.vue';
import Schedule from './views/Schedule.vue';
import Teams from './views/Teams.vue';
import Admin from './views/Admin.vue';

Vue.use(Router);

const router = new Router({
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
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
    },
    {
      path: '/admin/leagues',
      name: 'admin-leagues',
      component: Admin,
    },
    {
      path: '/admin/teams',
      name: 'admin-teams',
      component: Admin,
    },
    {
      path: '/admin/players',
      name: 'admin-players',
      component: Admin,
    },
  ],
});

router.beforeEach((to, from, next) => {
  next();
});

export default router;
