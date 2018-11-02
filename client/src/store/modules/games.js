import GamesService from '@/service/GamesService';

// state
const state = {
  games: [],
  selectedGameId: null,
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
};

// actions
const actions = {
  getLeagueGames({ commit }, leagueId) {
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
      }
    });
  },
  setSelectedGameId({ commit }, newId) {
    commit('mutateSelectedGameId', newId);
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
};

export default {
  state,
  getters,
  actions,
  mutations,
};
