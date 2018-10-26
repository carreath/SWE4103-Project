import Vue from 'vue';
import Vuex from 'vuex';

import globals from './modules/globals';
import user from './modules/user';
import leagues from './modules/leagues';
import teams from './modules/teams';
import players from './modules/players';
import games from './modules/games';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    globals,
    user,
    leagues,
    teams,
    players,
    games,
  },
});
