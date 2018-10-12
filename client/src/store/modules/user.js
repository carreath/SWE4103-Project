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
  userRegister({ commit }, payload) {
    delete payload.confirmPassword;
    return UserService.register(payload).then((response) => {
      console.log('RESPONSE: ', response);
      switch (response.status) {
        case 201:
          // TODO this is wrong - will have to log the user in
          commit('mutateUser', response.data);
          return { retVal: true, retMsg: 'Success' };
        case 409:
          return { retVal: false, retMsg: 'Email Already In Use' };
        default:
          return { retVal: false, retMsg: 'Server Error' };
      }
    });
  },
  userLogIn({ commit }, payload) {
    return UserService.login(payload).then((response) => {
      console.log('RESPONSE: ', response);
      switch (response.status) {
        case 200:
          commit('mutateUser', response.data);
          return { retVal: true, retMsg: 'Success' };
        case 404:
          return { retVal: false, retMsg: 'Email Not Registered' };
        case 403:
          return { retVal: false, retMsg: 'Invalid Credentials' };
        default:
          return { retVal: false, retMsg: 'Server Error' };
      }
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
