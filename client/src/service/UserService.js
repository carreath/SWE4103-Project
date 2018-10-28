import ServiceLayer from '@/service/ServiceLayer';

export default {
  register(params) {
    return ServiceLayer().post('/register', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  login(params) {
    return ServiceLayer().post('/login', params)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  getUserFromToken() {
    return ServiceLayer().get('/user')
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
  refreshToken() {
    return ServiceLayer().get('/token-check')
      .then((response) => {
        return response;
      })
      .catch((err) => {
        return err.response;
      });
  },
};
