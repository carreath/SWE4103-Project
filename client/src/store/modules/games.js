import GamesService from '@/service/GamesService';

// state
const state = {
  games: [
    {
      gameID: 0,
      leagueID: 1,
      homeTeamID: 1,
      awayTeamID: 2,
      refereeID: 1,
      field: 'Field A',
      gameTime: '2018-10-23 18:00:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 1,
      leagueID: 1,
      homeTeamID: 3,
      awayTeamID: 4,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-10-23 18:00:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 2,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-10-23 19:30:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 3,
      leagueID: 1,
      homeTeamID: 3,
      awayTeamID: 4,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-10-25 18:00:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 4,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-10-25 19:30:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 5,
      leagueID: 1,
      homeTeamID: 1,
      awayTeamID: 4,
      refereeID: 1,
      field: 'Field A',
      gameTime: '2018-10-30 18:00:00',
      status: 'Cancelled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 6,
      leagueID: 1,
      homeTeamID: 3,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-10-30 18:00:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 7,
      leagueID: 1,
      homeTeamID: 2,
      awayTeamID: 5,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-11-01 18:00:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 8,
      leagueID: 1,
      homeTeamID: 4,
      awayTeamID: 3,
      refereeID: 1,
      field: 'Field A',
      gameTime: '2018-11-01 19:30:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 9,
      leagueID: 1,
      homeTeamID: 6,
      awayTeamID: 1,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-11-01 19:30:00',
      status: 'Scheduled',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 10,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-10-18 18:00:00',
      status: 'Final',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 11,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-10-16 19:30:00',
      time: '19:30:00',
      status: 'Final',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 12,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      gameTime: '2018-10-18 19:30:00',
      status: 'Final',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 13,
      leagueID: 1,
      homeTeamID: null,
      awayTeamID: null,
      refereeID: null,
      field: 'Field B',
      gameTime: '2018-10-16 18:00:00',
      status: 'Open',
      homeGoals: 0,
      awayGoals: 0,
    },
    {
      gameID: 14,
      leagueID: 1,
      homeTeamID: null,
      awayTeamID: null,
      refereeID: null,
      field: 'Field A',
      gameTime: '2018-10-25 18:00:00',
      status: 'Open',
      homeGoals: 0,
      awayGoals: 0,
    },
  ],
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
  getGames({ commit }) {
    GamesService.getGames().then((response) => {
      if (response && response.status === 200) {
        commit('mutateGames', response.data.games);
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
};

export default {
  state,
  getters,
  actions,
  mutations,
};
