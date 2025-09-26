import FileUploadButton from '../components/FileUploadButton'
import TrainButton from '../components/TrainButton';
import { useState, useEffect } from 'react'
import { Container, Row, Col, Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

const Trainer = () => {
    const [selectedFiles, setSelectedFiles] = useState(null);
    const [option, setOption] = useState(null);
    const [metrics, setMetrics] = useState(null);
    const [refreshKey, setRefreshKey] = useState(0);
    const navigate = useNavigate();

    useEffect(() => {
        const storedMetrics = localStorage.getItem('metrics');
        const needsChartRefresh = localStorage.getItem('needsChartRefresh') === 'true';
        if (storedMetrics) {
            setMetrics(JSON.parse(storedMetrics));
        }
        if (needsChartRefresh) {
            setRefreshKey(prev => prev + 1);
            localStorage.removeItem('needsChartRefresh');
        }
    }, []);

    const handleFileSelect = (files, selectedOption) => {
        setSelectedFiles(files);
        setOption(selectedOption);
        localStorage.removeItem('metrics');
    };

    const handleUseExistingClick = () => {
        setSelectedFiles(null);
        setOption("useExisting");
        localStorage.removeItem('metrics');
    };

    const handleComplete = (result) => {
        if (result.chunks) {
            localStorage.setItem("labelChunks", JSON.stringify(result.chunks));
            navigate('/label');
        } else if (result.metrics) {
            setMetrics(result.metrics);
            localStorage.setItem("metrics", JSON.stringify(result.metrics));
            setRefreshKey(prev => prev + 1);
        }
    };

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
                        />
                        <FileUploadButton
                            onFileSelect={(files) => handleFileSelect(files, "customJson")}
                            forTrain={true}
                            label="Upload json file with categorized chunks"
                        />
                        <Button
                            variant="light"
                            className="text-dark select-btn"
                            onClick={handleUseExistingClick}
                        >
                            <i className="bi bi-upload pe-2 fs-5"></i>
                            <span>Use existing training data</span>
                        </Button>
                    </div>
                </Col>
            </Row>
            <Row className="pt-5 px-3">
                <h4 className="fs-4 mb-4">Evaluation Metrics</h4>

                <Col md={6}>
                    <img
                    src={`/visualization/metrics.png?key=${refreshKey}`}
                    alt="Training Metrics"
                    style={{ width: '100%', height: 'auto' }}
                    />
                </Col>

                <Col md={6}>
                    <img
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