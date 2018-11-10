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
};
