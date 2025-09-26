import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css';
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DashboardLayout from './layouts/DashboardLayout';
import Home from './pages/Home';
import Analyzer from './pages/Analyzer';
import Trainer from './pages/Trainer';
import Labeler from './pages/Labeler';

function App() {
  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={
            <DashboardLayout>
              <Home />
            </DashboardLayout>
          }
        />
        <Route
          path="/analyze"
          element={
            <DashboardLayout>
              <Analyzer />
            </DashboardLayout>
          }
        />
        <Route
          path="/train"
          element={
            <DashboardLayout>
              <Trainer />
            </DashboardLayout>
          }
        />
        <Route
          path="/label"
          element={
            <DashboardLayout>
              <Labeler />
            </DashboardLayout>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;