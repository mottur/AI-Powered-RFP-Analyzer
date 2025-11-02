/*
Links the frontend and backend using axios. 
Defines an 'apiService' that can execute the api functions from the backend.
*/

import { err } from '../services/utils';
import axios from 'axios';


const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5050';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 50000,
});

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

    const response = await api.post('/classification/train/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  // Get status of training
  getTrainingStatus: async () => {
    const response = await api.get('/classification/status/');
    return response.data; // returns { status, chunks }
  },

  // Save labeled chunks to file
  saveLabels: async (labeledChunks) => {
    try {
      const response = await api.post('/validation/labeled-chunks/', labeledChunks, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      return response.data;
    } catch (error) {
      err('Failed to save labels: ', error);
      throw error;
    }
  },

  // Extract text from PDF, chunk, and classify
  classifyText: async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await api.post('/classification/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data; // returns { session_id, categories, mlflow_run_id }
  },

  // Validate extracted content
  validateExtraction: async (chunks) => {
    const response = await api.post('/validation/', chunks);
    return response.data; // returns labeled chunks
  },

  // Get status of validation
  getValidationStatus: async () => {
    const response = await api.get('/validation/status/');
    return response.data; // returns status
  },

  // Summarize content
  summarizeText: async (sessionId) => {
    const response = await api.post('/summarization/', null, {
      params: { session_id: sessionId },
    });
    return response.data;
  },
};

export default api;