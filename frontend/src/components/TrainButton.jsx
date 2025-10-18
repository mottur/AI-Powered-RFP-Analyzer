/*
Component for executing the classifier training backend code.
*/

import { Button, Spinner } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import { apiService } from '../services/api';
import { updateIsTraining, pollTrainingStatus, err } from '../services/utils';

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

    updateIsTraining(true);

    try {
      await apiService.trainClassifier(files, option);

      let result = await pollTrainingStatus(apiService);

      if (onComplete) {
        onComplete(result);
      }
    } catch (error) {
      updateIsTraining(false);
      setLoading(false);
      err('Failed to train classifier: ', error);
      alert('Error processing the document.');
    } finally {
      // For customPdfs, we only extract text here — actual training happens after labeling
      if (option != "customPdfs") {
        updateIsTraining(false);
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