// state
const state = {
  player: [], // NOTE: idk
};

// getters
const getters = {
  playersByTeamId: (state) => (id) => {
    return state.players.filter(player => player.teamId === id);
  },
};

// actions
const actions = {

};

// mutations
const mutations = {

};

export default {
  state,
  getters,
  actions,
  mutations,
};
