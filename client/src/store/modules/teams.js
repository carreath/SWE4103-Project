import TeamsService from '@/service/TeamsService';

// state
const state = {
  teams: [],
  selectedTeamId: null, // NOTE this should default to first team in selecetd league
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
    return state.teams.find(team => team.teamID === state.selectedTeamId);
  },
  teamById: (state) => (teamId) => {
    return state.teams.find(team => team.teamID === teamId) || {};
  },
  teamsByLeagueId: (state) => (leagueId) => {
    return state.teams.filter(team => team.leagueID === leagueId);
  },
};

// actions
const actions = {
  getTeams({ commit }) {
    TeamsService.getTeams().then((response) => {
      if (response && response.status === 200) {
        commit('mutateTeams', response.data.teams);
      }
    });
  },
  setSelectedTeamId({ getters, dispatch, commit }, id) {
    commit('mutateSelectedTeamId', id);
    if (id &&
      getters.selectedGame &&
      getters.selectedGame.homeTeamID !== id &&
      getters.selectedGame.awayTeamID !== id) {
      dispatch('setSelectedGameId', null);
    }
  },
  createTeam({ getters, dispatch }, teamObj) {
    teamObj.leagueID = getters.selectedLeagueId;
    return TeamsService.createTeam(teamObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          // TODO this probs wont be right
          // commit('addTeam', response.data.team);
          dispatch('getTeams');
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
