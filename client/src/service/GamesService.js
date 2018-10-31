import ServiceLayer from '@/service/ServiceLayer';

export default {
  getGames() {
    return ServiceLayer().get('/game-schedule')
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
