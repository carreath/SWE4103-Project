import ServiceLayer from '@/service/ServiceLayer';

export default {
  register(params) {
    return ServiceLayer().post('/user/register', params)
      .then((response) => {
        // Successfully registered
        console.log('Response: ', response);
        return response;
      })
      .catch((err) => {
        // Register Not Successfull
        // TODO actually handle the error
        console.log('Err: ', err);
        return err;
      });
  },
  login(params) {
    return ServiceLayer().post('/user/login', params)
      .then((response) => {
        // Successfully logged in
        return response;
      })
      .catch((err) => {
        // Login not successfull
        // TODO actually handle the error
        err = {
          id: '1',
          firstName: 'Ben',
          lastName: 'Rombaut',
          email: 'rombaut.benj@gmail.com',
        };
        return err;
      });
  },
};
