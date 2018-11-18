import PlayersService from '@/service/PlayersService';

// state
const state = {
  players: [], // NOTE: idk
};

// getters
const getters = {
  players(state) {
    return state.players;
  },
  playersByTeamId: (state) => (id) => {
    return state.players.filter(player => player.teamId === id);
  },
};

// actions
const actions = {
  getPlayers({ commit }) {
    PlayersService.getPlayers().then((response) => {
      if (response && response.status === 200) {
        commit('mutatePlayers', response.data.players);
      }
    });
  },

};

// mutations
const mutations = {
  mutatePlayers(state, payload) {
    state.players = payload;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
