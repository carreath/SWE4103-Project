import TeamsService from '@/service/TeamsService';

// state
const state = {
  teams: [ // NOTE this is hardcoded until the backend gets their shit together
    {
      teamID: 1,
      leagueID: 1,
      managerID: 1,
      teamName: 'Team1',
      colour: '#4b89ed',
      leaguePoints: 0,
      wins: 0,
      losses: 0,
      draws: 0,
    },
    {
      teamID: 2,
      leagueID: 1,
      managerID: 2,
      teamName: 'Team2',
      leaguePoints: 0,
      wins: 0,
      losses: 0,
      draws: 0,
    },
    {
      teamID: 3,
      leagueID: 1,
      managerID: 3,
      teamName: 'Team3',
      leaguePoints: 0,
      wins: 0,
      losses: 0,
      draws: 0,
    },
    {
      teamID: 4,
      leagueID: 1,
      managerID: 4,
      teamName: 'Team4',
      leaguePoints: 0,
      wins: 0,
      losses: 0,
      draws: 0,
    },
    {
      teamID: 5,
      leagueID: 1,
      managerID: 5,
      teamName: 'Team5',
      leaguePoints: 0,
      wins: 0,
      losses: 0,
      draws: 0,
    },
    {
      teamID: 6,
      leagueId: 1,
      managerId: 6,
      teamName: 'Team6',
      leaguePoints: 0,
      wins: 0,
      losses: 0,
      draws: 0,
    },
  ],
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
    return state.teams.find(team => team.teamID === teamId);
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
        commit('mutateTeams', response.teams);
      }
    });
  },
  setSelectedTeamId({ getters, dispatch, commit }, id) {
    commit('mutateSelectedTeamId', id);
    if (getters.selectedGame &&
      getters.selectedGame.homeTeamID !== id &&
      getters.selectedGame.awayTeamID !== id) {
      dispatch('setSelectedGameId', null);
    }
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
