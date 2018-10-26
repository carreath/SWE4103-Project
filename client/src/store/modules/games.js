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
      date: '2018-10-23',
      time: '18:00:00',
      status: 'Scheduled',
    },
    {
      gameID: 1,
      leagueID: 1,
      homeTeamID: 3,
      awayTeamID: 4,
      refereeID: 1,
      field: 'Field B',
      date: '2018-10-23',
      time: '18:00:00',
      status: 'Scheduled',
    },
    {
      gameID: 2,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      date: '2018-10-23',
      time: '19:30:00',
      status: 'Scheduled',
    },
    {
      gameID: 3,
      leagueID: 1,
      homeTeamID: 3,
      awayTeamID: 4,
      refereeID: 1,
      field: 'Field B',
      date: '2018-10-25',
      time: '18:00:00',
      status: 'Scheduled',
    },
    {
      gameID: 4,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      date: '2018-10-25',
      time: '19:30:00',
      status: 'Scheduled',
    },
    {
      gameID: 5,
      leagueID: 1,
      homeTeamID: 1,
      awayTeamID: 4,
      refereeID: 1,
      field: 'Field A',
      date: '2018-10-30',
      time: '18:00:00',
      status: 'Cancelled',
    },
    {
      gameID: 6,
      leagueID: 1,
      homeTeamID: 3,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      date: '2018-10-30',
      time: '18:00:00',
      status: 'Scheduled',
    },
    {
      gameID: 7,
      leagueID: 1,
      homeTeamID: 2,
      awayTeamID: 5,
      refereeID: 1,
      field: 'Field B',
      date: '2018-11-01',
      time: '18:00:00',
      status: 'Scheduled',
    },
    {
      gameID: 8,
      leagueID: 1,
      homeTeamID: 4,
      awayTeamID: 3,
      refereeID: 1,
      field: 'Field A',
      date: '2018-11-01',
      time: '19:30:00',
      status: 'Scheduled',
    },
    {
      gameID: 9,
      leagueID: 1,
      homeTeamID: 6,
      awayTeamID: 1,
      refereeID: 1,
      field: 'Field B',
      date: '2018-11-01',
      time: '19:30:00',
      status: 'Scheduled',
    },
    {
      gameID: 10,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      date: '2018-10-23',
      time: '19:30:00',
      status: 'Scheduled',
    },
    {
      gameID: 11,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      date: '2018-10-23',
      time: '19:30:00',
      status: 'Scheduled',
    },
    {
      gameID: 12,
      leagueID: 1,
      homeTeamID: 5,
      awayTeamID: 6,
      refereeID: 1,
      field: 'Field B',
      date: '2018-10-23',
      time: '19:30:00',
      status: 'Scheduled',
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
};

// actions
const actions = {
  setSelectedGameId({ commit }, newId) {
    commit('mutateSelectedGameId', newId);
  },
};

// mutations
const mutations = {
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
