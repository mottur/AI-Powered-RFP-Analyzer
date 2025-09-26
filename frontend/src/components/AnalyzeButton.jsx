import { Button, Spinner } from 'react-bootstrap';
import { useState } from 'react';
import { apiService } from '../services/api';

const AnalyzeButton = ({ file = null, onComplete }) => {
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    if (!file) {
      alert('Please select a file first.');
      return;
    }

    setLoading(true);

    try {
      const extractResult = await apiService.extractText(file);
      const sessionId = extractResult.session_id;

      const summaryResult = await apiService.summarizeText(sessionId);

      if (onComplete) {
        onComplete({
          sessionId,
          categories: extractResult.categories,
          summaries: summaryResult.summaries,
        });
      }
    } catch (error) {
      console.error('Failed to extract and summarize:', error);
      alert('Error processing the document.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Button variant="light" onClick={handleClick} disabled={loading || !file} className="text-dark go-btn">
        {loading ? <span className="analyzing-text">Analyzing document  <Spinner animation="border" size="sm" /></span> : <i className="bi bi-arrow-right pe-2 fs-5"></i>}
    </Button>
  );
};

export default AnalyzeButton;