import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    // Fetch patients from API
    setPatients([
      { id: 1, name: 'John Doe', dob: '1980-01-01' },
      { id: 2, name: 'Jane Doe', dob: '1990-02-02' }
    ]);
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <ul>
        {patients.map(patient => (
          <li key={patient.id}>
            <Link to={`/patient/${patient.id}`}>{patient.name}</Link>
          </li>
        ))}
      </ul>
      <Link to="/upload">Upload CSV</Link>
    </div>
  );
};

export default Dashboard;
