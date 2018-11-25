import ScheduleService from '@/service/ScheduleService';

// state
const state = {
  fieldAvaiability: [], // NOTE: idk
};

// actions
const actions = {
  getSchedule({ commit }) {
    ScheduleService.getSchedule().then((response) => {
      if (response && response.status === 200) {
        commit('mutateSchedule', response.data.fieldAvaiability);
      }
    });
  },
  createSchedule({ dispatch }, scheduleObj) {
    return ScheduleService.createSchedule(scheduleObj).then((response) => {
      if (!response || !response.status) {
        return { retVal: false, retMsg: 'Server Error' };
      }

      switch (response.status) {
        case 201: {
          dispatch('getSchedule');
          return { retVal: true, retMsg: 'Schedule Created' };
        }
        default: {
          return { retVal: false, retMsg: 'Server Error' };
        }
      }
    });
  },
};

// mutations
const mutations = {
  mutateSchedule(state, payload) {
    state.fieldAvaiability = payload;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
