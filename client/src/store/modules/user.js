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
};

const actions = {
  userRegister({ dispatch }, payload) {
    return UserService.register(payload).then((response) => {
      console.log('RESPONSE: ', response);
      switch (response.status) {
        case 201: {
          // TODO handle this better
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
      console.log('RESPONSE: ', response);
      switch (response.status) {
        case 201: {
          const mToken = response.data.token;
          localStorage.setItem('token', mToken);
          // TODO remeber to actually change this to the response.data.user field
          // commit('mutateUser', response.data.user);
          const tempUser = {
            firstName: payload.email.split('@')[0],
            lastName: payload.email.split('@')[1],
            email: payload.email,
          };
          commit('mutateUser', tempUser);
          commit('mutateToken', mToken);
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
};

const mutations = {
  mutateUser(state, payload) {
    state.user = payload;
  },
  mutateToken(state, token) {
    state.token = token;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
