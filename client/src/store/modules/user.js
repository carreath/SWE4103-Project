import UserService from '@/service/UserService';

const state = {
  user: null,
  token: localStorage.getItem('token') || null,
};

const getters = {
  user(state) {
    return state.user;
  },
  token(state) {
    return state.token;
  },
  loggedIn(state) {
    return state.token && state.user;
  },
};

const actions = {
  userRegister({ dispatch }, payload) {
    return UserService.register(payload).then((response) => {
      switch (response.status) {
        case 201: {
          const loginPayload = {
            email: payload.email,
            password: payload.password,
          };
          return dispatch('userLogIn', loginPayload).then((retObj) => {
            return retObj;
          });
        }
        case 409: {
          return { retVal: false, retMsg: 'Email Already In Use' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  userLogIn({ commit }, payload) {
    return UserService.login(payload).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }
      switch (response.status) {
        case 201: {
          commit('mutateUser', response.data.user);
          commit('mutateToken', response.data.token);
          return { retVal: true, retMsg: 'Success' };
        }
        case 404: {
          return { retVal: false, retMsg: 'Email Not Registered' };
        }
        case 403: {
          return { retVal: false, retMsg: 'Invalid Credentials' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
  userLogOut({ commit }) {
    commit('mutateUser', null);
    commit('mutateToken', null);
  },
  setUser({ commit }, user) {
    commit('mutateUser', user);
  },
  retrieveUserFromToken({ commit, dispatch }) {
    UserService.getUserFromToken().then((response) => {
      if (response.status && response.status === 200) {
        dispatch('refreshToken');
        commit('mutateUser', response.data.user);
      } else {
        commit('mutateUser', null);
        commit('mutateToken', null);
      }
    });
  },
  refreshToken({ commit }) {
    UserService.refreshToken().then((response) => {
      if (response.status && response.status === 200) {
        commit('mutateToken', response.data.token);
      } else {
        commit('mutateToken', null);
      }
    });
  },
};

const mutations = {
  mutateUser(state, payload) {
    state.user = payload;
  },
  mutateToken(state, token) {
    token ? localStorage.setItem('token', token) : localStorage.removeItem('token');
    state.token = token;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
