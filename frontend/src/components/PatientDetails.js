import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PatientDetails = () => {
  const { id } = useParams();
  const [patient, setPatient] = useState(null);
  const [records, setRecords] = useState([]);

  useEffect(() => {
    // Fetch patient details and records from API
    setPatient({ id: 1, name: 'John Doe', dob: '1980-01-01' });
    setRecords([
      { id: 1, date: '2023-01-01', data: 'Record 1 data' },
      { id: 2, date: '2023-02-01', data: 'Record 2 data' }
    ]);
  }, [id]);

  if (!patient) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{patient.name}</h1>
      <p>Date of Birth: {patient.dob}</p>
      <h2>Records</h2>
      <ul>
        {records.map(record => (
          <li key={record.id}>{record.date}: {record.data}</li>
        ))}
      </ul>
    </div>
  );
};

export default PatientDetails;
