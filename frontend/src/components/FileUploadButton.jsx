import { Button } from 'react-bootstrap';
import { useRef, useState, useEffect } from 'react';

const FileUploadButton = ({ onFileSelect, selectedFileName = null, forTrain = false, label = 'Upload document(s)' }) => {
  const fileInputRef = useRef(null);
  const [fileName, setFileName] = useState(selectedFileName || null);

  // Sync internal state with prop changes
  useEffect(() => {
    setFileName(selectedFileName || null);
  }, [selectedFileName]);

  const handleButtonClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (event) => {
    const files = Array.from(event.target.files);
    if (files.length > 0 && onFileSelect) {
      if (!forTrain && files.length > 1) {
        alert('Please select only one file.');
        fileInputRef.current.value = ''; // reset file input
        return;
      }
      if (!forTrain && files.length === 1) {
        setFileName(files[0].name);
      } else {
        setFileName(null);
      }

      onFileSelect(files); // Send all files to parent
    }
  };

  const getButtonLabel = () => {
    if (forTrain) {
      return label;
    } else if (fileName) {
      return fileName;
    } else {
      return 'Upload a new document';
    }
  };

  return (
    <>
      <input
        type="file"
        accept=".pdf,.json"
        multiple
        ref={fileInputRef}
        onChange={handleFileChange}
        style={{ display: 'none' }}
      />
      <Button variant="light" className="text-dark select-btn" onClick={handleButtonClick}>
        <i className="bi bi-upload pe-2 fs-5"></i>
        <span>{getButtonLabel()}</span>
      </Button>
    </>
  );
};

export default FileUploadButton;