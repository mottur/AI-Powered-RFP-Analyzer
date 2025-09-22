import axios from 'axios';

// Vite uses import.meta.env for environment variables
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized access
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const apiService = {
  // Health check
  healthCheck: async () => {
    try {
      const response = await api.get('/');
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Items endpoints
  getItems: async () => {
    try {
      const response = await api.get('/api/items');
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  createItem: async (itemData) => {
    try {
      const response = await api.post('/api/items', itemData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // User endpoints
  getUser: async (userId) => {
    try {
      const response = await api.get(`/api/users/${userId}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default api;