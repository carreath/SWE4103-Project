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
    return UserService.login(payload).then((response) => {
      console.log('RESPONSE: ', response);
      // TODO will need check here to see if login was successfull
      if (response) {
        commit('mutateUser', response);
        return true;
      }
      return false;
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
