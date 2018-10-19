import ServiceLayer from '@/service/ServiceLayer';

export default {
  getTeams() {
    return ServiceLayer().get('/teams')
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  createTeam(params) {
    return ServiceLayer().post('/teams', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
