
// state
const state = {
  loginModalVisible: false,
  createAccoundModalVisible: false,
  editLeagueModalVisible: false,
  editTeamModalVisible: false,
  editPlayerModalVisible: false,
  scheduleSelectedView: 'Table',
};

// getters
const getters = {
  modalVisible(state) {
    return state.loginModalVisible || state.createAccoundModalVisible;
  },
  editModalVisible(state) {
    return state.editLeagueModalVisible || state.editTeamModalVisible
    || state.editPlayerModalVisible;
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
  editTeamModalVisible(state) {
    return state.editTeamModalVisible;
  },
  editPlayerModalVisible(state) {
    return state.editPlayerModalVisible;
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
    dispatch('getPlayers');
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
    commit('mutateEditTeamModalVisible', false);
    commit('mutateEditPlayerModalVisible', false);
  },
  setEditTeamModalVisible({ commit }, isVisible) {
    commit('mutateEditTeamModalVisible', isVisible);
    commit('mutateEditLeagueModalVisible', false);
    commit('mutateEditPlayerModalVisible', false);
  },
  setEditPlayerModalVisible({ commit }, isVisible) {
    commit('mutateEditPlayerModalVisible', isVisible);
    commit('mutateEditLeagueModalVisible', false);
    commit('mutateEditTeamModalVisible', false);
  },
  closeModal({ dispatch }) {
    dispatch('setLoginModalVisible', false);
    dispatch('setCreateAccountModalVisible', false);
    dispatch('setEditLeagueModalVisible', false);
    dispatch('setEditTeamModalVisible', false);
    dispatch('setEditPlayerModalVisible', false);
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
  mutateEditTeamModalVisible(state, isVisible) {
    state.editTeamModalVisible = isVisible;
  },
  mutateEditPlayerModalVisible(state, isVisible) {
    state.editPlayerModalVisible = isVisible;
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
