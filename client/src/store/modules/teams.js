import TeamsService from '@/service/TeamsService';

// state
const state = {
  teams: [],
  selectedTeamId: null, // NOTE this should default to first team in selecetd league
  editedTeamId: 1,
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
  editedTeamId(state) {
    return state.editedTeamId;
  },
  editedTeam(state) {
    return state.teams.find(team => team.teamID === state.editedTeamId);
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
  setEditedTeam({ commit }, id) {
    commit('mutateEditedTeamId', id);
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
  deleteTeam({ dispatch }, teamObj) {
    const params = {
      teamID: teamObj.teamID,
    };
    return TeamsService.deleteTeam(params).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getTeams');
          return { retVal: true, retMsg: 'Team Deleted' };
        }
        case 400: {
          return { retVal: false, retMsg: 'Team Cannot Be Deleted If They Have Played A Game' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  editTeam({ dispatch }, teamObj) {
    return TeamsService.editTeam(teamObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getTeams');
          return { retVal: true, retMsg: 'Team Edited' };
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
  mutateEditedTeamId(state, id) {
    state.editedTeamId = id;
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
