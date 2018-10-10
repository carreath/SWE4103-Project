import UserService from '@/service/UserService';

const state = {
  user: null,
};

const getters = {
  user(state) {
    return state.user;
  },
};

const actions = {
  userLogIn({ commit }, payload) {
    UserService.login(payload).then((response) => {
      console.log('RESPONSE: ', response);
      commit('mutateUser', response);
    });
  },
  userLogOut({ commit }) {
    commit('mutateUser', null);
  },
};

const mutations = {
  mutateUser(state, payload) {
    state.user = payload;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
