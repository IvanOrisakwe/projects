
import React, { useState, useEffect } from 'react';
import BicycleCard from '../components/BicycleCard';
import BicycleService from '../services/BicycleService';

function BicycleListPage() {
  const [bicycles, setBicycles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchBicycles();
  }, []);

  const fetchBicycles = async () => {
    try {
      setLoading(true);
      const data = await BicycleService.getAllBicycles();
      setBicycles(data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch bicycles. Please try again later.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = (id) => {
    setBicycles(bicycles.filter(bike => bike.id !== id));
  };

  if (loading) {
    return (
      <div className="d-flex justify-content-center">
        <div className="spinner-border" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="alert alert-danger" role="alert">
        {error}
      </div>
    );
  }

  return (
    <div>
      <h2>Bicycle Sales Announcements</h2>
      
      {bicycles.length === 0 ? (
        <div className="alert alert-info">
          No bicycles for sale. Add some on the other page!
        </div>
      ) : (
        <div className="row row-cols-1 row-cols-md-3 g-4">
          {bicycles.map(bicycle => (
            <div key={bicycle.id} className="col">
              <BicycleCard bicycle={bicycle} onDelete={handleDelete} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default BicycleListPage;