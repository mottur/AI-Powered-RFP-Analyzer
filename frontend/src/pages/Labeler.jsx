import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Row, Col, Card, Form, Button } from 'react-bootstrap';
import { apiService } from '../services/api';

const LABELS = {
    "Scope": "This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.",
    "Deliverables": "This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.",
    "Company Info": "This section provides information about the offeror/contractor, including qualifications, past experience, and mission.",
    "Timeline": "This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.",
    "Technologies": "This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project.",
}

const Labeler = () => {
  const [chunks, setChunks] = useState([]);
  const [labels, setLabels] = useState({});
  const navigate = useNavigate();

  useEffect(() => {
    const saved = localStorage.getItem('labelChunks');
    if (saved) {
      setChunks(JSON.parse(saved));
    } else {
      alert("No chunks to label. Redirecting...");
      navigate('/trainer');
    }
  }, [navigate]);

  const handleLabelChange = (index, newLabel) => {
    setLabels((prev) => ({
      ...prev,
      [index]: newLabel,
    }));
  };

  const handleSubmit = async () => {
    const labeledChunks = chunks.map((chunk, index) => ({
      ...chunk,
      true_label: labels[index] !== '__SKIP__' ? labels[index] : null,
    }));

    localStorage.removeItem('metrics');
    localStorage.setItem('needsChartRefresh', 'false');
    localStorage.setItem('isTraining', 'true');

    try {
        // 1. Save labeled chunks
        await apiService.saveLabels(labeledChunks);

        // 2. Trigger training using existing labels
        const metrics = await apiService.trainClassifier();

        // 3. Store metrics in localStorage so Trainer page can load them
        localStorage.setItem('metrics', JSON.stringify(metrics));
        localStorage.setItem('needsChartRefresh', 'true');
        localStorage.setItem('isTraining', 'false');

        // 4. Redirect to Trainer page
        navigate('/train');
    } catch (error) {
        if (error.code === 'ECONNABORTED') {
            // Timeout occurred — but training might still be ongoing
            console.warn('Training timeout — continuing assuming backend is still working.');
        } else {
            console.error('Error during label submission and training:', error);
            alert('Something went wrong while submitting labels or training.');
            localStorage.setItem('isTraining', 'false');
            navigate('/train');
        }
    }

    // Poll localStorage for metrics
    try {
      const metrics = await pollForMetrics();
      localStorage.setItem('isTraining', 'false');
      localStorage.setItem('needsChartRefresh', 'true');
      navigate('/train');
    } catch (error) {
      console.warn('Metrics not found after polling:', error);
      alert('Training is likely still running. Please check the Trainer page soon.');
      localStorage.setItem('isTraining', 'true');
    }
  };

  const pollForMetrics = async (retries = 24, delayMs = 5000) => {
    for (let i = 0; i < retries; i++) {
      const raw = localStorage.getItem('metrics');
      if (raw) {
        try {
          const metrics = JSON.parse(raw);
          return metrics;
        } catch (e) {
          console.warn("Invalid metrics format — retrying...");
        }
      }
      await new Promise((res) => setTimeout(res, delayMs));
    }
    throw new Error('Metrics not found after polling localStorage.');
  };

  return (
    <Container fluid className="p-4">
      <Row>
        <Col>
          <div className="d-flex flex-row justify-content-between align-items-center gap-4 w-100">
            <h2 className="fs-4">Manually label chunks from custom dataset</h2>
            <Button
              variant="light"
              className="mb-3 ms-auto text-dark go-btn"
              onClick={handleSubmit}
              disabled={chunks.length === 0}
            >
              <i className="bi bi-send pe-2 fs-5"></i>
              <span>Submit Labels and Train</span>
            </Button>
          </div>
        </Col>
      </Row>

      {chunks.map((chunk, index) => (
        <Card key={index} className="mb-4">
          <Card.Body>
            <h5>{chunk.title}</h5>
            <p>{chunk.body}</p>

            <Form.Select
              value={labels[index] || ""}
              onChange={(e) => handleLabelChange(index, e.target.value)}
            >
              <option value="">Select label</option>
              {Object.keys(LABELS).map((labelKey) => (
                <option key={labelKey} value={labelKey}>
                  {labelKey}
                </option>
              ))}
              <option value="__SKIP__">N/A</option>
            </Form.Select>
          </Card.Body>
        </Card>
      ))}
    </Container>
  );
};

export default Labeler;