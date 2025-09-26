import Category from '../components/Category'
import FileUploadButton from '../components/FileUploadButton'
import AnalyzeButton from '../components/AnalyzeButton';
import { useState, useEffect } from 'react'
import { Container, Row, Col } from 'react-bootstrap';

const Analyzer = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [selectedFileName, setSelectedFileName] = useState(null);
    const [results, setResults] = useState(null);

    useEffect(() => {
        const storedResults = localStorage.getItem('rfpResults');
        if (storedResults) {
        setResults(JSON.parse(storedResults));
        }
        const storedFileName = localStorage.getItem('selectedFileName');
        if (storedFileName && storedFileName !== 'undefined') {
        setSelectedFileName(storedFileName);
        }
    }, []);

    const handleFileSelect = (files) => {
        const file = files[0];
        if (!file) return;

        setSelectedFile(file);
        setSelectedFileName(file.name);
        setResults(null);
        localStorage.removeItem('rfpResults');
        localStorage.setItem('selectedFileName', file.name);
    };


    const handleComplete = ({ sessionId, categories, summaries }) => {
        const newResults = { sessionId, categories, summaries };
        setResults(newResults);
        localStorage.setItem('rfpResults', JSON.stringify(newResults));
    };

    return (
        <Container fluid className="p-0">
            <Row className="p-3">
                <Col>
                    <div className="d-flex flex-row justify-content-between align-items-center gap-4 w-100">
                        <h1 className="fs-3">Analyze an RFP document</h1>
                        <AnalyzeButton file={selectedFile} onComplete={handleComplete} />
                    </div>
                    <div className="d-flex flex-column justify-content-center gap-4 pt-4 w-100">
                        <FileUploadButton onFileSelect={handleFileSelect} selectedFileName={selectedFileName} />

                        {results && results.summaries && (() => {
                            return Object.entries(results.summaries).map(([title, summary]) => {
                                const keywordObj = results.categories?.[title]?.keywords || {};
                                const keywordsArray = Object.values(keywordObj).flat(); // Flatten all keyword arrays
                                const keywords = keywordsArray.join(', ') || 'N/A';

                                return (
                                <Category
                                    key={title}
                                    title={title}
                                    keywords={keywords}
                                    summary={summary}
                                />
                                );
                            });
                        })()}

                    </div>
                </Col>
            </Row>
        </Container>
    )
}

export default Analyzer;
