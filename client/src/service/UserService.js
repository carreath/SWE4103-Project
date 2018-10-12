import ServiceLayer from '@/service/ServiceLayer';

export default {
  register(params) {
    return ServiceLayer().post('/register', params)
      .then((response) => {
        console.log('Register Success: ', response);
        return response;
      })
      .catch((err) => {
        console.log('Register Err: ', err);
        return err;
      });
  },
  login(params) {
    return ServiceLayer().post('/login', params)
      .then((response) => {
        console.log('Login Success: ', response);
        return response;
      })
      .catch((err) => {
        console.log('Login Err: ', err);
        return err;
      });
  },
};
