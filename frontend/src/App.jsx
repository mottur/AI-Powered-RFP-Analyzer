import { useState, useEffect } from 'react'
import Categories from './components/Categories'
import { apiService } from './services/api'
import './App.css'
import { Button, Navbar, Nav, Card, Container } from 'react-bootstrap';

function App() {
  const [backendStatus, setBackendStatus] = useState('checking')
  const [healthData, setHealthData] = useState(null)
  const [activeTab, setActiveTab] = useState('categories')

  useEffect(() => {
    checkBackendHealth()
  }, [])

  const checkBackendHealth = async () => {
    try {
      const data = await apiService.healthCheck()
      setHealthData(data)
      setBackendStatus('connected')
    } catch (error) {
      setBackendStatus('disconnected')
      console.error('Backend connection failed:', error)
    }
  }

  const renderTabContent = () => {
    switch (activeTab) {
      case 'categories':
        return <Categories />
      case 'health':
        return (
          <div className="health-check">
            <h3>Backend Health Status</h3>
            <div className={`status-badge ${backendStatus}`}>
              {backendStatus.toUpperCase()}
            </div>
            {healthData && (
              <div className="health-data">
                <pre>{JSON.stringify(healthData, null, 2)}</pre>
              </div>
            )}
            <button 
              onClick={checkBackendHealth} 
              className="btn-secondary"
            >
              Re-check Health
            </button>
          </div>
        )
      default:
        return <ItemList />
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>React + FastAPI App</h1>
        <div className="backend-status">
          <span className="status-label">Backend: </span>
          <span className={`status ${backendStatus}`}>
            {backendStatus.toUpperCase()}
          </span>
        </div>
      </header>

      <nav className="tabs">
        <button 
          className={activeTab === 'categories' ? 'tab active' : 'tab'}
          onClick={() => setActiveTab('categories')}
        >
          Categories
        </button>
        <button 
          className={activeTab === 'health' ? 'tab active' : 'tab'}
          onClick={() => setActiveTab('health')}
        >
          Health Check
        </button>
      </nav>

      <main className="app-main">
        {renderTabContent()}
      </main>

      <footer className="app-footer">
        <p>Frontend: React + Vite | Backend: FastAPI</p>
        {backendStatus === 'disconnected' && (
          <div className="connection-help">
            <p>⚠️ Make sure your FastAPI server is running on port 8000:</p>
            <code>uvicorn main:app --reload --port 8000</code>
          </div>
        )}
      </footer>
    </div>
  )
}

export default App
