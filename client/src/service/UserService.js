import ServiceLayer from '@/service/ServiceLayer';

export default {
  login(params) {
    console.log('PARAMS: ', params);
    return ServiceLayer().post('/login', params).then((response) => {
      console.log('serviceResponse: ', response);
      return response;
    });
  },
};
