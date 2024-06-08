import React, { useState } from 'react';

const FileUpload = () => {
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (file) {
      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await fetch('http://localhost:5000/api/upload', { // Adjust URL based on your Flask backend URL
          method: 'POST',
          body: formData,
        });
        if (response.ok) {
          alert('File uploaded successfully');
        } else {
          alert('Failed to upload file');
        }
      } catch (error) {
        console.error('Error uploading file:', error);
        alert('Error uploading file');
      }
    } else {
      alert('Please select a file');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Upload CSV</label>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} required />
      </div>
      <button type="submit">Upload</button>
    </form>
  );
};

export default FileUpload;
