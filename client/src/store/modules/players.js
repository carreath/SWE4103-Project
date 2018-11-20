import PlayersService from '@/service/PlayersService';

// state
const state = {
  players: [], // NOTE: idk
  editedPlayerId: 1,
};

// getters
const getters = {
  players(state) {
    return state.players;
  },
  playersByTeamId: (state) => (id) => {
    return state.players.filter(player => player.teamId === id);
  },
  playerById: (state) => (playerId) => {
    return state.players.find(player => player.playerID === playerId);
  },
  editedPlayerId(state) {
    return state.editedPlayerId;
  },
  editedPlayer(state) {
    return state.players.find(player => player.playerID === state.editedPlayerId);
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
  setEditedPlayer({ commit }, id) {
    commit('mutateEditedPlayerId', id);
  },
  deletePlayer({ dispatch }, playerObj) {
    const params = {
      playerID: playerObj.playerID,
    };
    return PlayersService.deletePlayer(params).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getPlayers');
          return { retVal: true, retMsg: 'Player Deleted' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  editPlayer({ dispatch }, playerObj) {
    return PlayersService.editPlayer(playerObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getPlayers');
          return { retVal: true, retMsg: 'Player Edited' };
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
  mutateEditedPlayerId(state, id) {
    state.editedPlayerId = id;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
