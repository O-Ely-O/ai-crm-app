import axios, { type AxiosInstance } from "axios";

export const TOKEN_KEY = "ttp_crm_token";

const baseURL =
  import.meta.env.VITE_API_URL || "http://localhost:8000/api";

const api: AxiosInstance = axios.create({
  baseURL,
  headers: { "Content-Type": "application/json" },
  withCredentials: false,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem(TOKEN_KEY);
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      localStorage.removeItem(TOKEN_KEY);
    }
    return Promise.reject(err);
  }
);

export default api;