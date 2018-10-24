// state
const state = {
  games: [
    {
      id: 0,
      homeTeam: 'TeamA',
      awayTeam: 'TeamB',
      leagueId: 1,
      fieldName: 'Field A',
      date: '2018-10-23',
      time: '18:00:00',
    },
    {
      id: 1,
      homeTeam: 'TeamC',
      awayTeam: 'TeamD',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-10-23',
      time: '18:00:00',
    },
    {
      id: 2,
      homeTeam: 'TeamX',
      awayTeam: 'TeamY',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-10-23',
      time: '19:30:00',
    },
    {
      id: 3,
      homeTeam: 'TeamC',
      awayTeam: 'TeamD',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-10-25',
      time: '18:00:00',
    },
    {
      id: 4,
      homeTeam: 'TeamX',
      awayTeam: 'TeamY',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-10-25',
      time: '19:30:00',
    },
    {
      id: 5,
      homeTeam: 'TeamA',
      awayTeam: 'TeamD',
      leagueId: 1,
      fieldName: 'Field A',
      date: '2018-10-30',
      time: '18:00:00',
    },
    {
      id: 6,
      homeTeam: 'TeamC',
      awayTeam: 'TeamY',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-10-30',
      time: '18:00:00',
    },
    {
      id: 7,
      homeTeam: 'TeamB',
      awayTeam: 'TeamX',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-11-01',
      time: '18:00:00',
    },
    {
      id: 8,
      homeTeam: 'TeamD',
      awayTeam: 'TeamC',
      leagueId: 1,
      fieldName: 'Field A',
      date: '2018-11-01',
      time: '19:30:00',
    },
    {
      id: 9,
      homeTeam: 'TeamY',
      awayTeam: 'TeamA',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-11-01',
      time: '19:30:00',
    },
    {
      id: 10,
      homeTeam: 'TeamX',
      awayTeam: 'TeamY',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-10-23',
      time: '19:30:00',
    },
    {
      id: 11,
      homeTeam: 'TeamX',
      awayTeam: 'TeamY',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-10-23',
      time: '19:30:00',
    },
    {
      id: 12,
      homeTeam: 'TeamX',
      awayTeam: 'TeamY',
      leagueId: 1,
      fieldName: 'Field B',
      date: '2018-10-23',
      time: '19:30:00',
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
    console.log('selectedGame: ', state.games.find((game) => game.id === state.selectedGameId));
    return state.games.find((game) => game.id === state.selectedGameId);
  },
  gameById: (state) => (gameId) => {
    return state.games.filter(game => game.gameId === gameId);
  },
  gamesByLeagueId: (state) => (leagueId) => {
    return state.games.filter(game => game.leagueId === leagueId);
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
