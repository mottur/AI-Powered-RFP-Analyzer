import { Container, Row, Col, Button } from 'react-bootstrap';
import { NavLink } from 'react-router-dom';

const Home = () => {
    return (
        <Container fluid className="p-0">
            <Row className="p-3">
                <Col>
                    <h1 className="fs-3">Welcome to APRA, the AI-Powered RFP Analyzer!</h1>
                    <div className="d-flex flex-column justify-content-center flex-md-row gap-4 pt-4 w-100">
                        <Button as={NavLink} to="/analyze" variant="light" className="text-dark select-btn">Analyze a document</Button>
                        <Button as={NavLink} to="/train" variant="light" className="text-dark select-btn">Train the classifier on your documents</Button>
                    </div>
                </Col>
            </Row>
        </Container>
    )
}
export default Home;