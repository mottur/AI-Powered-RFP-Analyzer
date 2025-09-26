import Sidebar from '../components/Sidebar';
import { apiService } from '../services/api';
import { useState, useEffect } from 'react'

const DashboardLayout = ({ children }) => {
  const [backendStatus, setBackendStatus] = useState('checking');
  const [healthData, setHealthData] = useState(null);

  useEffect(() => {
    checkBackendHealth();
  }, []);

  const checkBackendHealth = async () => {
    try {
      const data = await apiService.healthCheck();
      setHealthData(data);
      setBackendStatus('connected');
    } catch (error) {
      setBackendStatus('disconnected');
      console.error('Backend connection failed:', error);
    }
  };

  return (
    <div>
      <div className="sidebar">
        <Sidebar />
      </div>

      <div className="main-content" style={{ minHeight: '100vh' }}>
        <header className="app-header text-end p-3 border-bottom">
          <div className="backend-status">
            <span className="status-label">Backend: </span>
            <span className={`status ${backendStatus}`}>
              {backendStatus.toUpperCase()}
            </span>
          </div>
        </header>
  
        <main className="p-4">
          {children}
        </main>

        <footer className="app-footer text-center p-3 mb-auto border-top">
             <p className="mb-1 fs-6">Frontend: React | Backend: FastAPI</p>
             {backendStatus === 'disconnected' && (
              <div className="connection-help">
                <p>⚠️ Make sure your FastAPI server is running on port 8000:</p>
                <code>uvicorn main:app --reload --port 8000</code>
              </div>
            )}
          </footer>
      </div>
    </div>
  );
};

export default DashboardLayout;