
// state
const state = {
  loginModalVisible: false,
  createAccoundModalVisible: false,
  activeNavIndex: '1',
};

// getters
const getters = {
  modalVisible(state) {
    return state.loginModalVisible || state.createAccoundModalVisible;
  },
  loginModalVisible(state) {
    return state.loginModalVisible;
  },
  createAccoundModalVisible(state) {
    return state.createAccoundModalVisible;
  },
  activeNavIndex(state) {
    return state.activeNavIndex;
  },
};

// actions
const actions = {
  setLoginModalVisible({ commit }, isVisible) {
    commit('mutateCreateAccountModalVisible', false);
    commit('mutateLoginModalVisible', isVisible);
  },
  setCreateAccountModalVisible({ commit }, isVisible) {
    commit('mutateLoginModalVisible', false);
    commit('mutateCreateAccountModalVisible', isVisible);
  },
  closeModal({ dispatch }) {
    dispatch('setLoginModalVisible', false);
    dispatch('setCreateAccountModalVisible', false);
  },
  setActiveNavIndex({ commit }, index) {
    commit('mutateActiveNavIndex', index);
  },
};

// mutations
const mutations = {
  mutateLoginModalVisible(state, isVisible) {
    state.loginModalVisible = isVisible;
  },
  mutateCreateAccountModalVisible(state, isVisible) {
    state.createAccoundModalVisible = isVisible;
  },
  mutateActiveNavIndex(state, index) {
    state.activeNavIndex = index;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
