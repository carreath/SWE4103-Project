import ServiceLayer from '@/service/ServiceLayer';

export default {
  login(params) {
    console.log('PARAMS: ', params);
    return ServiceLayer().post('/login', params)
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
        console.log(err);
        return err;
      });
  },
};
