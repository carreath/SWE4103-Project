import UserService from '@/service/UserService';

const state = {
  user: null,
  token: localStorage.getItem('token') || null,
  users: null,
  editedUserId: null,
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
  users(state) {
    return state.users;
  },
  editedUserId(state) {
    return state.editedUserId;
  },
  editedUser(state) {
    return state.users.find(user => user.userID === state.editedUserId);
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
  userLogIn({ commit, dispatch }, payload) {
    return UserService.login(payload).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }
      switch (response.status) {
        case 201: {
          commit('mutateUser', response.data.user);
          commit('mutateToken', response.data.token);
          if (response.data.user.userType === 'Admin') {
            dispatch('getAllUsers');
          }
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
    commit('mutateUsers', null);
  },
  setUser({ commit }, user) {
    commit('mutateUser', user);
  },
  setEditedUser({ commit }, id) {
    commit('mutateEditedUserId', id);
  },
  retrieveUserFromToken({ commit, dispatch }) {
    UserService.getUserFromToken().then((response) => {
      if (response.status && response.status === 200) {
        dispatch('refreshToken');
        commit('mutateUser', response.data.user);
        if (response.data.user.userType === 'Admin') {
          commit('mutateUsers', response.data.users);
        }
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
  validateToken() {
    return UserService.getUserFromToken().then((response) => {
      if (response.status && response.status === 200) {
        return response.data.user;
      }
      return null;
    });
  },
  getAllUsers({ commit }) {
    UserService.getUserFromToken().then((response) => {
      if (response.status && response.status === 200 && response.data.user.userType === 'Admin') {
        commit('mutateUsers', response.data.users);
      } else {
        commit('mutateUsers', null);
      }
    });
  },
  editUser({ getters, dispatch }, userObj) {
    console.log('EDITUSER: ', userObj);
    return UserService.editUser(userObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 200 || 201: {
          getters.user.userID === userObj.userID ? dispatch('retrieveUserFromToken') : dispatch('getAllUsers');
          return { retVal: true, retMsg: 'User Edited' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
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
  mutateUsers(state, payload) {
    state.users = payload;
  },
  mutateEditedUserId(state, id) {
    state.editedUserId = id;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
