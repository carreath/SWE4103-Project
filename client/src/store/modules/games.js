import GamesService from '@/service/GamesService';

// state
const state = {
  games: [],
  selectedGameId: null,
  gameRosters: [],
};

// getters
const getters = {
  games(state) {
    return state.games;
  },
  selectedGameId(state) {
    return state.selectedGameId;
  },
  selectedGame(state) {
    return state.games.find((game) => game.gameID === state.selectedGameId);
  },
  gameById: (state) => (gameId) => {
    return state.games.filter(game => game.gameID === gameId);
  },
  gamesByLeagueId: (state) => (leagueId) => {
    return state.games.filter(game => game.leagueID === leagueId);
  },
  gamesByTeamId: (state) => (teamId) => {
    return state.games.filter(game => game.homeTeamID === teamId || game.awayTeamID === teamId);
  },
  gamesSortedByDate(state) {
    const retObj = {};
    state.games.forEach((game) => {
      const gameDay = game.gameTime.split(' ')[0];
      if (retObj[gameDay]) {
        retObj[gameDay].push(game);
      } else {
        retObj[gameDay] = [game];
      }
    });
    return retObj;
  },
  gamesByLeagueIdSortedByDate: (state, getters) => (leagueId) => {
    const retObj = {};
    getters.gamesByLeagueId(leagueId).forEach((game) => {
      const gameDay = game.gameTime.split(' ')[0];
      if (retObj[gameDay]) {
        retObj[gameDay].push(game);
      } else {
        retObj[gameDay] = [game];
      }
    });
    return retObj;
  },
  gamesByTeamIdSortedByDate: (state, getters) => (teamId) => {
    const retObj = {};
    getters.gamesByTeamId(teamId).forEach((game) => {
      const gameDay = game.gameTime.split(' ')[0];
      if (retObj[gameDay]) {
        retObj[gameDay].push(game);
      } else {
        retObj[gameDay] = [game];
      }
    });
    return retObj;
  },
  gameRosters(state) {
    return state.gameRosters;
  },
  gameRosterByGameID: (state) => (gameID) => {
    return state.gameRosters.filter(gameRoster => gameRoster.gameID === gameID);
  },
};

// actions
const actions = {
  getLeagueGames({ dispatch, commit }, leagueId) {
    const payload = {
      leagueID: leagueId,
    };
    GamesService.getGames(payload).then((response) => {
      if (response && response.status === 200) {
        const commitPaylaod = {
          leagueID: leagueId,
          games: response.data.games,
        };
        commit('addLeagueGames', commitPaylaod);
        dispatch('getAllGameRosters');
      }
    });
  },
  getAllGameRosters({ getters, commit }) {
    getters.games.forEach(game => {
      const payload = {
        gameID: game.gameID,
      };
      console.log('payload: ', payload);
      GamesService.getGameRoster(payload).then((response) => {
        if (response && response.status === 200) {
          const commitPayload = {
            gameID: game.gameID,
            ...response.data['game-roster'],
          };
          console.log('commitPay', commitPayload);
          commit('addGameRoster', commitPayload);
        }
      });
    });
  },
  setSelectedGameId({ commit }, newId) {
    commit('mutateSelectedGameId', newId);
  },
  createGame({ getters, dispatch }, gameObj) {
    gameObj.leagueID = getters.selectedLeagueId;
    return GamesService.createGame(gameObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          // TODO this probs wont be right
          // commit('addGame', response.data.game);
          dispatch('getGames');
          return { retVal: true, retMsg: 'Game Created' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  editGame({ dispatch }, gameObj) {
    return GamesService.editGame(gameObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getLeagueGames', gameObj.leagueID);
          return { retVal: true, retMsg: 'Game Edited' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  submitGameRoster({ getters, dispatch }, params) {
    const submitParams = {
      gameID: params.gameID,
      data: params,
    };
    return GamesService.submitGameRoster(submitParams).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getLeagueGames', getters.selectedLeagueId);
          return { retVal: true, retMsg: 'Game Edited' };
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
  mutateGames(state, payload) {
    state.games = payload;
  },
  mutateSelectedGameId(state, id) {
    state.selectedGameId = id;
  },
  addLeagueGames(state, payload) {
    state.games = state.games.filter(game => game.leagueID !== payload.leagueID);
    state.games.push(...payload.games);
  },
  addGameRoster(state, payload) {
    state.gameRosters = state.gameRosters.filter(gameRoster => {
      return gameRoster.gameID !== payload.gameID;
    });
    state.gameRosters.push(payload);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
