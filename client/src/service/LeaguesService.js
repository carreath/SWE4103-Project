import ServiceLayer from '@/service/ServiceLayer';

export default {
  getLeagues() {
    return ServiceLayer().get('/leagues')
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  createLeague(params) {
    return ServiceLayer().post('/leagues', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
