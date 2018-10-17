import LeaguesService from '@/service/LeaguesService';

// state
const state = {
  leagues: [
    {
      id: 1,
      name: 'League1',
      season: '2018',
    },
    {
      id: 2,
      name: 'League2',
      season: '2018',
    },
  ],
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
};

// actions
const actions = {
  getLeagues({ commit }) {
    LeaguesService.getLeagues().then((response) => {
      if (response && response.status === 200) {
        commit('mustateLeagues', response.leagues);
      }
    });
  },
  setSelectedLeague({ commit }, id) {
    commit('mutateSelectedLeagueId', id);
  },
  createLeague({ commit }, leagueObj) {
    LeaguesService.createLeague(leagueObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          // TODO this probs wont be right
          commit('addLeague', response.newLeague);
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
  mustateLeagues(state, payload) {
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
