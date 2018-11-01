import axios from 'axios';
import store from '@/store/index';

export default() => {
  let host = process.env.VUE_APP_HOST;

  return axios.create({
    baseURL: `${host}/api`,
    withCredentials: false,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      Authorization: store.getters.token,
    },
  });
};
