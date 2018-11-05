
// state
const state = {
  loginModalVisible: false,
  createAccoundModalVisible: false,
  editLeagueModalVisible: false,
  scheduleSelectedView: 'Table',
};

// getters
const getters = {
  modalVisible(state) {
    return state.loginModalVisible || state.createAccoundModalVisible;
  },
  editModalVisible(state) {
    return state.editLeagueModalVisible;
  },
  loginModalVisible(state) {
    return state.loginModalVisible;
  },
  createAccoundModalVisible(state) {
    return state.createAccoundModalVisible;
  },
  editLeagueModalVisible(state) {
    return state.editLeagueModalVisible;
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
  setEditLeagueModalVisible({ commit }, isVisible) {
    commit('mutateEditLeagueModalVisible', isVisible);
  },
  closeModal({ dispatch }) {
    dispatch('setLoginModalVisible', false);
    dispatch('setCreateAccountModalVisible', false);
    dispatch('setEditLeagueModalVisible', false);
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
  mutateEditLeagueModalVisible(state, isVisible) {
    state.editLeagueModalVisible = isVisible;
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
