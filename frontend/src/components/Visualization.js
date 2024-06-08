import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const Visualization = () => {
  const { id } = useParams();
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://localhost:5000/api/visualize/${id}`); // Adjust URL based on your Flask backend URL
        if (response.ok) {
          const result = await response.json();
          setData(result.visualization_data);
        } else {
          console.error('Failed to fetch visualization data');
        }
      } catch (error) {
        console.error('Error fetching visualization data:', error);
      }
    };

    fetchData();
  }, [id]);

  return (
    <div>
      <h1>Visualization for Patient {id}</h1>
      <div id="visualization">
        {/* Render visualization data here */}
        <p>Placeholder for visualization</p>
        {/* Example: Render data as JSON */}
        <pre>{JSON.stringify(data, null, 2)}</pre>
      </div>
    </div>
  );
};

export default Visualization;
