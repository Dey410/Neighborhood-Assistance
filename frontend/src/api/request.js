import axios from "axios";

const request = axios.create({
  baseURL: "https://fastapi.xiaozhu410.cn/api",
  timeout: 10000,
});

export default request;
