import FileUploadButton from '../components/FileUploadButton'
import TrainButton from '../components/TrainButton';
import { useState, useEffect } from 'react'
import { Container, Row, Col, Button, Modal } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import { apiService } from '../services/api';

const Trainer = () => {
    const [selectedFiles, setSelectedFiles] = useState(null);
    const [option, setOption] = useState(null);
    const [metrics, setMetrics] = useState(null);
    const [refreshKey, setRefreshKey] = useState(Date.now());
    const [showModal, setShowModal] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        const storedMetrics = localStorage.getItem('metrics');
        const needsChartRefresh = localStorage.getItem('needsChartRefresh') === 'true';
        if (storedMetrics) {
            setMetrics(JSON.parse(storedMetrics));
        }
        if (needsChartRefresh) {
            setRefreshKey(Date.now());
            localStorage.removeItem('needsChartRefresh');
        }
    }, []);

    const handleFileSelect = (files, selectedOption) => {
        setSelectedFiles(files);
        setOption(selectedOption);
        localStorage.removeItem('metrics');
        localStorage.setItem("isTraining", "false");
        window.dispatchEvent(new Event("training-update"));
    };

    const handleUseExistingClick = () => {
        setSelectedFiles(null);
        setOption("useExisting");
        localStorage.removeItem('metrics');
    };

    const handleComplete = (result) => {
        if (result.chunks) {
            setShowModal(true);
            localStorage.setItem("labelChunks", JSON.stringify(result.chunks));
        } else if (result.metrics) {
            setMetrics(result.metrics);
            localStorage.setItem("metrics", JSON.stringify(result.metrics));
            setRefreshKey(Date.now());
        }
    };

    const handleModalManualConfirm = () => {
        setShowModal(false);
        navigate('/label');
    }

    const handleModalLLMConfirm = async () => {
        setShowModal(false);
        try {
            // 1. Label using an LLM and save labeled chunks
            const chunks = localStorage.getItem("labelChunks");
            const result = await apiService.validateExtraction(JSON.parse(chunks));
            await apiService.saveLabels(result.chunks);

            // 2. Trigger training using existing labels
            const metrics = await apiService.trainClassifier();

            // 3. Store metrics
            setMetrics(metrics);
            localStorage.setItem("metrics", JSON.stringify(result.metrics));
            setRefreshKey(Date.now());
        } catch (error) {
            if (error.code === 'ECONNABORTED') {
                // Timeout occurred — but training might still be ongoing
                console.warn('Training timeout — continuing assuming backend is still working.');
            } else {
                console.error('Error during label validation and training:', error);
                alert('Something went wrong while validating labels using LLM or training.');
            }
        } finally {
            localStorage.setItem("isTraining", "false");
            window.dispatchEvent(new Event("training-update"));
        }
    }

    return (
        <Container fluid className="p-0">
            <Row className="p-3">
                <Col>
                    <div className="d-flex flex-row justify-content-between align-items-center gap-4 w-100">
                        <h1 className="fs-3">Train the classifier on a custom dataset</h1>
                        <TrainButton files={selectedFiles} option={option} onComplete={handleComplete} />
                    </div>
                    <div className="d-flex flex-column justify-content-center gap-4 pt-4 w-100">
                        <FileUploadButton
                            onFileSelect={(files) => handleFileSelect(files, "customPdfs")}
                            forTrain={true}
                            label="Upload pdf files of training documents"
                            isSelected={option === "customPdfs"}
                        />
                        <FileUploadButton
                            onFileSelect={(files) => handleFileSelect(files, "customJson")}
                            forTrain={true}
                            label="Upload json file with categorized chunks"
                            isSelected={option === "customJson"}
                        />
                        <Button
                            variant="light"
                            className={`text-dark select-btn ${option === "useExisting" ? "selected" : ""}`}
                            onClick={handleUseExistingClick}
                        >
                            <i className="bi bi-upload pe-2 fs-5"></i>
                            <span>Use existing training data</span>
                        </Button>
                    </div>
                    <Modal show={showModal} onHide={() => setShowModal(false)} centered>
                        <Modal.Header closeButton>
                            <Modal.Title>Text Extraction Complete</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>
                            The extraction process has finished successfully.
                            Would you like to start labeling now?
                        </Modal.Body>
                        <Modal.Footer>
                            <Button variant="secondary" onClick={() => setShowModal(false)}>
                                Cancel
                            </Button>
                            <Button variant="light" onClick={handleModalLLMConfirm}>
                                Label using an LLM
                            </Button>
                            <Button variant="light" onClick={handleModalManualConfirm}>
                                Label manually
                            </Button>
                        </Modal.Footer>
                    </Modal>
                </Col>
            </Row>
            <Row className="pt-5 px-3">
                <h4 className="fs-4 mb-4">Evaluation Metrics</h4>

                <Col md={6}>
                    <img
                    key={`metrics-${refreshKey}`}
                    src={`/visualization/metrics.png?key=${refreshKey}`}
                    alt="Training Metrics"
                    style={{ width: '100%', height: 'auto' }}
                    />
                </Col>

                <Col md={6}>
                    <img
                    key={`matrix-${refreshKey}`}
                    src={`/visualization/confusion_matrix.png?key=${refreshKey}`}
                    alt="Confusion Matrix"
                    style={{ width: '100%', height: 'auto' }}
                    />
                </Col>
            </Row>
        </Container>
    );
};

export default Trainer;