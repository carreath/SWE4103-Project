// state
const state = {
  teams: [
    {
      teamId: 1,
      leagueId: 1,
      managerId: 1,
      teamName: 'Team1',
      leaguePoints: 2,
      wins: 1,
      losses: 0,
      draws: 0,
    },
    {
      teamId: 2,
      leagueId: 1,
      managerId: 2,
      teamName: 'Team2',
      leaguePoints: 0,
      wins: 0,
      losses: 1,
      draws: 0,
    },
    {
      teamId: 3,
      leagueId: 2,
      managerId: 3,
      teamName: 'Team3',
      leaguePoints: 0,
      wins: 0,
      losses: 0,
      draws: 0,
    },
  ],
};

// getters
const getters = {
  teams(state) {
    return state.teams;
  },
};

// actions
const actions = {
  getTeams() {

  },
};

// mutations
const mutations = {
  mustateTeams(state, payload) {
    state.teams = payload;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
