import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 20000,
});

// Optional: Add token-based auth if needed
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const apiService = {
  // Health check
  healthCheck: async () => {
    const response = await api.get('/');
    return response.data;
  },

  // Train classifier
  trainClassifier: async (files, option = 'useExisting') => {
    const formData = new FormData();
    if (Array.isArray(files) && files.length > 0) {
      files.forEach((file) => {
        formData.append('files', file);
      });
    }

    formData.append('option', option);

    const response = await api.post('/train-classifier/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  saveLabels: async (labeledChunks) => {
    try {
      const response = await api.post('/save-labels/', labeledChunks, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      return response.data;
    } catch (error) {
      console.error('Failed to save labels: ', error);
      throw error;
    }
  },

  // Extract text from PDF
  extractText: async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await api.post('/extract-text/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data; // returns { session_id, categories, mlflow_run_id }
  },

  // Validate extracted content
  validateExtraction: async (sessionId) => {
    const response = await api.post('/validate-extraction/', null, {
      params: { session_id: sessionId },
    });
    return response.data; // returns updated categories
  },

  // Summarize content
  summarizeText: async (sessionId) => {
    const response = await api.post('/summarize-text/', null, {
      params: { session_id: sessionId },
    });
    return response.data;
  },
};

export default api;