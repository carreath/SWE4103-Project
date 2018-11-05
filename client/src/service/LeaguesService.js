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
  deleteLeague(params) {
    return ServiceLayer().delete('/league', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  editLeague(params) {
    return ServiceLayer().put('/league', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
