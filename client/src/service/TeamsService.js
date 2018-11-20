import ServiceLayer from '@/service/ServiceLayer';

export default {
  getTeams() {
    return ServiceLayer().get('/team')
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  createTeam(params) {
    return ServiceLayer().post('/team', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  deleteTeam(paramsIn) {
    return ServiceLayer().delete('/team', { params: paramsIn })
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  editTeam(params) {
    return ServiceLayer().put('/team', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
