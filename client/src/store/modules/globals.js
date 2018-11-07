
// state
const state = {
  loginModalVisible: false,
  createAccoundModalVisible: false,
  scheduleSelectedView: 'Table',
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
  scheduleSelectedView(state) {
    return state.scheduleSelectedView;
  },
};

// actions
const actions = {
  getAllData({ dispatch }) {
    dispatch('getLeagues');
    dispatch('getTeams');
  },
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
  setScheduleSelectedView({ commit }, newView) {
    commit('mutateLoginScheduleSelectedView', newView);
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
  mutateLoginScheduleSelectedView(state, newView) {
    state.scheduleSelectedView = newView;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
