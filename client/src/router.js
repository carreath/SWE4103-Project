import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import PasswordReset from './views/PasswordReset.vue';
import Standings from './views/Standings.vue';
import Schedule from './views/Schedule.vue';
import Teams from './views/Teams.vue';
import Admin from './views/Admin.vue';

import store from './store/index';
import ScheduleGameCreate from './components/ScheduleGameCreate.vue';
import CreateScheduleForm from './components/CreateScheduleForm.vue';

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
      path: '/schedule/game',
      name: 'schedule-game',
      component: Schedule,
    },
    {
      path: '/schedule/create',
      name: 'create-schedule-form',
      component: CreateScheduleForm,
    },
    {
      path: '/schedule/game/create',
      name: 'schedule-game-create',
      component: ScheduleGameCreate,
    },
    {
      path: '/teams',
      name: 'teams',
      component: Teams,
    },
    {
      path: '/teams/:teamID',
      name: 'teams-page',
      component: Teams,
    },

    /*
    {
      path: '/schedule/game/create',
      name: 'schedule-game-create',
      component: ScheduleGameCreate,
      beforeEnter: (to, from, next) => {
        const user = store.getters.user;
        if (user) {
          switch (user.userType) {
            case ('Admin'):
              next('/schedule/game/create');
              break;
            case ('Coordinator'):
              next('/schedule/game/create');
              break;
            default:
              next('/');
          }
          return;
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user) {
              next('/schedule/game/create');
            } else {
              next('/');
            }
          });
        }
        next('/');
      },
    },
    */
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      beforeEnter: (to, from, next) => {
        const user = store.getters.user;
        if (user) {
          switch (user.userType) {
            case ('Admin'):
              next('/admin/leagues');
              break;
            case ('Coordinator'):
              next('/admin/leagues');
              break;
            case ('Manager'):
              next('/admin/teams');
              break;
            default:
              next('/');
          }
          return;
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user) {
              switch (user.userType) {
                case ('Admin'):
                  next('/admin/leagues');
                  break;
                case ('Coordinator'):
                  next('/admin/leagues');
                  break;
                case ('Manager'):
                  next('/admin/teams');
                  break;
                default:
                  next('/');
              }
            } else {
              next('/');
            }
          });
        }
        next('/');
      },
    },
    {
      path: '/admin/leagues',
      name: 'admin-leagues',
      component: Admin,
      beforeEnter: (to, from, next) => {
        const user = store.getters.user;
        if (user && (user.userType === 'Admin' || user.userType === 'Coordinator')) {
          next();
          return;
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && (user.userType === 'Admin' || user.userType === 'Coordinator')) {
              next();
            } else {
              next('/');
            }
          });
        } else {
          next('/');
        }
      },
    },
    {
      path: '/admin/teams',
      name: 'admin-teams',
      component: Admin,
      beforeEnter: (to, from, next) => {
        const user = store.getters.user;
        if (user && (user.userType === 'Admin' || user.userType === 'Coordinator' || user.userType === 'Manager')) {
          next();
          return;
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && (user.userType === 'Admin' || user.userType === 'Coordinator' || user.userType === 'Manager')) {
              next();
            } else {
              next('/');
            }
          });
        } else {
          next('/');
        }
      },
    },
    {
      path: '/admin/players',
      name: 'admin-players',
      component: Admin,
      beforeEnter: (to, from, next) => {
        const user = store.getters.user;
        if (user && (user.userType === 'Admin' || user.userType === 'Coordinator' || user.userType === 'Manager')) {
          next();
          return;
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && (user.userType === 'Admin' || user.userType === 'Coordinator' || user.userType === 'Manager')) {
              next();
            } else {
              next('/');
            }
          });
        } else {
          next('/');
        }
      },
    },
    {
      path: '/admin/players/create',
      name: 'admin-players-create',
      component: Admin,
    },
    {
      path: '/admin/leagues/create',
      name: 'admin-leagues-create',
      component: Admin,
      beforeEnter: (to, from, next) => {
        const user = store.getters.user;
        if (user && (user.userType === 'Admin')) {
          next();
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && user.userType === 'Admin') {
              next();
            } else {
              next('/');
            }
          });
        } else {
          next('/');
        }
      },
    },
    {
      path: '/admin/teams/create',
      name: 'admin-teams-create',
      component: Admin,
      beforeEnter: (to, from, next) => {
        const user = store.getters.user;
        if (user && (user.userType === 'Admin' || user.userType === 'Coordinator')) {
          next();
          return;
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && (user.userType === 'Admin' || user.userType === 'Coordinator')) {
              next();
            } else {
              next('/');
            }
          });
        } else {
          next('/');
        }
      },
    },
    {
      path: '/admin/users',
      name: 'admin-users',
      component: Admin,
      beforeEnter: (to, from, next) => {
        const user = store.getters.user;
        if (user && (user.userType === 'Admin')) {
          next();
          return;
        }
        if (store.getters.token) {
          store.dispatch('validateToken').then((user) => {
            if (user && user.userType === 'Admin') {
              next();
            } else {
              next('/');
            }
          });
        } else {
          next('/');
        }
      },
    },
    {
      path: '*',
      name: 'default',
      beforeEnter: (to, from, next) => {
        next('/');
      },
    },
  ],
});

router.beforeEach((to, from, next) => {
  next();
});

export default router;
