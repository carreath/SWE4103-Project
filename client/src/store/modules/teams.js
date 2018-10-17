import TeamsService from '@/service/TeamsService';

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
  selectedTeamId: 1, // NOTE default to first teams
};

// getters
const getters = {
  teams(state) {
    return state.teams;
  },
  selectedTeamId(state) {
    return state.selectedTeamId;
  },
  selectedTeam(state) {
    return state.teams.find(team => team.id === state.selectedTeamId);
  },
  teamsByLeagueId: (state) => (leagueId) => {
    return state.teams.filter(team => team.leagueId === leagueId);
  },
};

// actions
const actions = {
  getTeams({ commit }) {
    TeamsService.getTeams().then((response) => {
      if (response && response.status === 200) {
        commit('mutateTeams', response.teams);
      }
    });
  },
  setSelectedTeamId({ commit }, id) {
    commit('mutateSelectedTeamId', id);
  },
  createTeam({ commit }, teamObj) {
    TeamsService.createTeam(teamObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          // TODO this probs wont be right
          commit('addTeam', response.newTeam);
          return { retVal: true, retMsg: 'Team Created' };
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
  mutateTeams(state, payload) {
    state.teams = payload;
  },
  mutateSelectedTeamId(state, id) {
    state.selectedTeamId = id;
  },
  addTeam(state, teamObj) {
    state.teams.push(teamObj);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
