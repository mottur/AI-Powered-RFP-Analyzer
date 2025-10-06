import { Button, Spinner } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import { apiService } from '../services/api';

const TrainButton = ({ files = null, option = "useExisting", onComplete }) => {
  const [loading, setLoading] = useState(() => {
    return localStorage.getItem("isTraining") === "true";
  });

  useEffect(() => {
    const handleStorageUpdate = () => {
      const isTraining = localStorage.getItem("isTraining") === "true";
      setLoading(isTraining);
    };

    window.addEventListener("training-update", handleStorageUpdate);

    return () => {
      window.removeEventListener("training-update", handleStorageUpdate);
    };
  }, []);

  const handleClick = async () => {
    if (option != "useExisting" && !files) {
      alert('Please select some training document(s) first.');
      return;
    }

    localStorage.setItem("isTraining", "true")
    window.dispatchEvent(new Event("training-update"));

    try {
      const results = await apiService.trainClassifier(files, option);

      if (onComplete) {
        onComplete(results);
      }
    } catch (error) {
      if (error.code === 'ECONNABORTED') {
          // Timeout occurred — but training might still be ongoing
          console.warn('Training timeout — continuing assuming backend is still working.');
      } else {
          console.error('Failed to train classifier:', error);
          alert('Error processing the document.');
      }
    } finally {
      if (option != "customPdfs") {
        localStorage.setItem("isTraining", "false")
        setLoading(false);
      }
    }
  };

  return (
    <Button variant="light" onClick={handleClick} disabled={loading || (option !== "useExisting" && !files)} className="text-dark go-btn">
        {loading ? <span className="training-text">Training classifier  <Spinner animation="border" size="sm" /></span> : <i className="bi bi-arrow-right pe-2 fs-5"></i>}
    </Button>
  );
};

export default TrainButton;