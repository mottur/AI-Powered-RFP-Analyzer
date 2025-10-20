/*
The "/train" page of the application. On this page, the classifier model is trained using user-provided documents.
*/

import FileUploadButton from '../components/FileUploadButton'
import TrainButton from '../components/TrainButton';
import { useState, useEffect } from 'react'
import { Container, Row, Col, Button, Modal } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import { apiService } from '../services/api';
import { updateIsTraining, pollValidationStatus, pollTrainingStatus, err } from '../services/utils';

const Trainer = () => {
    const [selectedFiles, setSelectedFiles] = useState(null);
    const [option, setOption] = useState(null);
    const [refreshKey, setRefreshKey] = useState(Date.now());
    const [showModal, setShowModal] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        const refreshCharts = () => {
            setRefreshKey(Date.now());
        };
        refreshCharts();
        updateIsTraining(false); // Reset training state on page load
        window.addEventListener("training-update", refreshCharts);
        return () => {
            window.removeEventListener("training-update", refreshCharts);
        };
    }, []);

    const handleFileSelect = (files, selectedOption) => {
        setSelectedFiles(files);
        setOption(selectedOption);
        updateIsTraining(false);
    };

    const handleUseExistingClick = () => {
        setSelectedFiles(null);
        setOption("useExisting");
        updateIsTraining(false);
    };

    const handleComplete = (result) => {
        if (result.chunks) {
            setShowModal(true);
            localStorage.setItem("labelChunks", JSON.stringify(result.chunks));
        }
    };

    const handleModalManualConfirm = () => {
        setShowModal(false);
        navigate('/label');
    }

    const handleModalLLMConfirm = async () => {
        setShowModal(false);
        try {
            // 1. Start validation in backend
            const chunks = localStorage.getItem("labelChunks");
            await apiService.validateExtraction(JSON.parse(chunks));

            // 2. Poll for validation status
            let result = await pollValidationStatus(apiService); // returns true when complete

            if (!result) {
                throw new Error("Validation did not complete successfully.");
            }

            // 3. Train using the saved, validated data
            await apiService.trainClassifier();

            // 4. Poll for training status
            result = await pollTrainingStatus(apiService); // returns true when complete

            if (!result) {
                throw new Error("Training did not complete successfully.");
            }
        } catch (error) {
            err('Error during LLM labeling or training:', error);
            alert('Something went wrong during LLM labeling or training.');
        } finally {
            updateIsTraining(false);
        }
    };

    const handleModalCancel = () => {
        setShowModal(false);
        updateIsTraining(false);
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
                    <Modal show={showModal} onHide={handleModalCancel} centered>
                        <Modal.Header closeButton>
                            <Modal.Title>Text Extraction Complete</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>
                            The extraction process has finished successfully.
                            Would you like to start labeling now?
                        </Modal.Body>
                        <Modal.Footer>
                            <Button variant="secondary" onClick={handleModalCancel}>
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
                    src={`http://localhost:5050/plots/metrics.png?ts=${refreshKey}`}
                    alt="Training Metrics"
                    style={{ width: '100%', height: 'auto' }}
                    />
                </Col>

                <Col md={6}>
                    <img
                    key={`matrix-${refreshKey}`}
                    src={`http://localhost:5050/plots/confusion_matrix.png?ts=${refreshKey}`}
                    alt="Confusion Matrix"
                    style={{ width: '100%', height: 'auto' }}
                    />
                </Col>
            </Row>
        </Container>
    );
};

export default Trainer;