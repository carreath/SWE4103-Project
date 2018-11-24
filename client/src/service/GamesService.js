import ServiceLayer from '@/service/ServiceLayer';

export default {
  getGames(paramsIn) {
    return ServiceLayer().get('/game-schedule', { params: paramsIn })
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  createGame(params) {
    return ServiceLayer().post('/game', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  editGame(params) {
    return ServiceLayer().put('/game-schedule', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
