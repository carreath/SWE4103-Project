import ServiceLayer from '@/service/ServiceLayer';

export default {
  getSchedule(paramsIn) {
    return ServiceLayer().get('/game-schedule', { params: paramsIn })
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  createSchedule(params) {
    return ServiceLayer().post('/game-schedule', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
