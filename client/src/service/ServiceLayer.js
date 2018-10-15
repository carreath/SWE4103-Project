import axios from 'axios';
import store from '@/store/index';

export default() => {
  return axios.create({
    baseURL: 'http://127.0.0.1:5000/api',
    withCredentials: false,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      Authorization: store.getters.token,
    },
  });
};
