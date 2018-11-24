import LeaguesService from '@/service/LeaguesService';

// state
const state = {
  leagues: [],
  selectedLeagueId: 1, // NOTE Default to first league
  editedLeagueId: 1,
};

// getters
const getters = {
  leagues(state) {
    return state.leagues;
  },
  selectedLeagueId(state) {
    return state.selectedLeagueId;
  },
  selectedLeague(state) {
    return state.leagues.find(league => league.leagueID === state.selectedLeagueId);
  },
  leagueById: (state) => (id) => {
    return state.leagues.find(league => league.leagueID === id) || {};
  },
  editedLeagueId(state) {
    return state.editedLeagueId;
  },
  editedLeague(state) {
    return state.leagues.find(league => league.leagueID === state.editedLeagueId);
  },
};

// actions
const actions = {
  getLeagues({ commit, dispatch }) {
    LeaguesService.getLeagues().then((response) => {
      if (response && response.status === 200) {
        commit('mutateLeagues', response.data.leagues);
        response.data.leagues.forEach((league) => {
          dispatch('getLeagueGames', league.leagueID);
        });
      }
    });
  },
  setSelectedLeague({ commit, dispatch }, id) {
    dispatch('setSelectedTeamId', null);
    dispatch('setSelectedGameId', null);
    commit('mutateSelectedLeagueId', id);
  },
  setEditedLeague({ commit }, id) {
    commit('mutateEditedLeagueId', id);
  },

  createLeague({ dispatch }, leagueObj) {
    return LeaguesService.createLeague(leagueObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          // TODO this probs wont be right
          // commit('addLeague', response.data.league);
          dispatch('getLeagues');
          return { retVal: true, retMsg: 'League Created' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  deleteLeague({ dispatch }, leagueObj) {
    const params = {
      leagueID: leagueObj.leagueID,
    };
    return LeaguesService.deleteLeague(params).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getLeagues');
          return { retVal: true, retMsg: 'League Deleted' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  editLeague({ dispatch }, leagueObj) {
    return LeaguesService.editLeague(leagueObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200: {
          dispatch('getLeagues');
          return { retVal: true, retMsg: 'League Edited' };
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
  mutateLeagues(state, payload) {
    state.leagues = payload;
  },
  mutateSelectedLeagueId(state, id) {
    state.selectedLeagueId = id;
  },
  mutateEditedLeagueId(state, id) {
    state.editedLeagueId = id;
  },
  addLeague(state, leagueObj) {
    state.leagues.push(leagueObj);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
