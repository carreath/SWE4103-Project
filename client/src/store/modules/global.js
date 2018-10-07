
// state
const state = {
  user: {},
  loginModalVisible: false,
};

// getters
const getters = {
  user: context => context.user,
  loginModalVisible: state => state.loginModalVisible,
};

// actions
const actions = {
  setLoginModalVisible({ commit }, isVisible) {
    commit('mutateLoginModalVisible', isVisible);
  },
};

// mutations
const mutations = {
  mutateLoginModalVisible(state, isVisible) {
    state.loginModalVisible = isVisible;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
