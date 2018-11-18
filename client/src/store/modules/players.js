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
  createPlayer({ dispatch }, playerObj) {
    return PlayersService.createPlayer(playerObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          dispatch('getPlayers');
          return { retVal: true, retMsg: 'Player Created' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
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
