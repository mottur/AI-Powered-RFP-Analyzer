import { Accordion } from 'react-bootstrap';

const Category = ({ title, keywords, summary }) => {
  const isInsights = title === "Insights";

  return (
    <Accordion defaultActiveKey={null} className="category">
      <Accordion.Item eventKey="0">
        <Accordion.Header className="fs-2">{title}</Accordion.Header>
        <Accordion.Body>
          {isInsights ? (
            <p>{summary}</p>
          ) : (
            <>
              <p><strong>Keywords:</strong> {keywords}</p>
              <p><strong>Summary:</strong> {summary}</p>
            </>
          )}
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
  );
};

export default Category;