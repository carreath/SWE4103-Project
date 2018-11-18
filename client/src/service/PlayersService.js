import ServiceLayer from '@/service/ServiceLayer';

export default {
  getPlayers() {
    return ServiceLayer().get('/player')
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  createPlayer(params) {
    return ServiceLayer().post('/player', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
