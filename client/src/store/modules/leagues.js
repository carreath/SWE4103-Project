import LeaguesService from '@/service/LeaguesService';

// state
const state = {
  leagues: [],
  selectedLeagueId: 1, // NOTE Default to first league
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
  setSelectedLeague({ commit }, id) {
    commit('mutateSelectedLeagueId', id);
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
};

// mutations
const mutations = {
  mutateLeagues(state, payload) {
    state.leagues = payload;
  },
  mutateSelectedLeagueId(state, id) {
    state.selectedLeagueId = id;
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
