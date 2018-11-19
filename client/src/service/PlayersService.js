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
  deletePlayer(params) {
    return ServiceLayer().delete('/player', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  editPlayer(params) {
    return ServiceLayer().put('/player', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
