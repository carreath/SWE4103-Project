import Vue from 'vue';
import Vuex from 'vuex';

import global from './modules/global';
import user from './modules/user';
import leagues from './modules/leagues';
import teams from './modules/teams';
import players from './modules/players';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    global,
    user,
    leagues,
    teams,
    players,
  },
});
