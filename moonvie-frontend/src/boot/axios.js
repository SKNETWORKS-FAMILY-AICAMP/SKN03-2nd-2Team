import { boot } from 'quasar/wrappers'
import axios from 'axios'

// axios.defaults.headers.common['Access-Control-Allow-Origin'] = [
// 'http://localhost:8000',   'http://192.168.210.129:8001',
// 'ws://192.168.210.129:8001',   'http://175.193.132.25:8001' ];
const BaseURL = location.host.split(':')[0]
const Port = 3000
// console.log(BaseURL, Port);
axios.defaults.withCredentials = true
// const http = axios.create({ baseURL: 'http://localhost:3000' });
const http = axios.create({ baseURL: `http://${BaseURL}:${Port}` })
/* http.interceptors.request.use(
  (config) => {
    config;
    console.log(config);
  },
  (error) => {
    Promise.reject(error);
  }
); */
export default boot(({ app }) => {
  /* axios */
  app.config.globalProperties.$axios = axios
  app.config.globalProperties.$api = http
})

export { http }
