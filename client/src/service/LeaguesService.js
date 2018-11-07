import ServiceLayer from '@/service/ServiceLayer';

export default {
  getLeagues() {
    return ServiceLayer().get('/league')
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  createLeague(params) {
    return ServiceLayer().post('/league', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
