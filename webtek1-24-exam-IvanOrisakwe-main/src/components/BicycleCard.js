import React, { useState } from 'react';
import BicycleService from '../services/BicycleService';

function BicycleCard({ bicycle, onDelete }) {
  const [deleting, setDeleting] = useState(false);
  const [error, setError] = useState(null);

  const handleBuyClick = async () => {
    if (window.confirm(`Are you sure you want to buy this ${bicycle.brand} ${bicycle.model}?`)) {
      try {
        setDeleting(true);
        setError(null);
        await BicycleService.deleteBicycle(bicycle.id);
        onDelete(bicycle.id);
      } catch (err) {
        setError('Failed to delete bicycle');
        console.error(err);
      } finally {
        setDeleting(false);
      }
    }
  };

  const hardcodedImageUrl = 'https://imgs.search.brave.com/5OtMRkNdIOU_SS5EcRPNDTJu6UD79JCuymc71Qt6REo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/c3RyaWN0bHliaWN5/Y2xlcy5jb20vY2Ru/L3Nob3AvZmlsZXMv/WTFScy1UZWFtTWFu/LWZvbmRvX25lcm8t/cHJvc3BldHRpdmFf/YW50ZXJpb3JlLmpw/Zz92PTE3MzM4Njc1/NDAmd2lkdGg9MTY4/MA';


  return (
    <div className="card mb-3">
      {error && (
        <div className="alert alert-danger m-2 p-2" role="alert">
          {error}
        </div>
      )}
      
      <img 
        src={hardcodedImageUrl} 
        className="card-img-top" 
        alt={`${bicycle.brand} ${bicycle.model}`} 
        style={{ height: '200px', objectFit: 'cover' }}
      />
      
      <div className="card-body">
        <h5 className="card-title">{bicycle.brand} {bicycle.model}</h5>
        <p className="card-text"><strong>Price:</strong> ${parseFloat(bicycle.price).toFixed(2)}</p>
        {bicycle.additionalInfo && (
          <p className="card-text">{bicycle.additionalInfo}</p>
        )}
        <button 
          className="btn btn-primary" 
          onClick={handleBuyClick}
          disabled={deleting}
        >
          {deleting ? (
            <>
              <span className="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
              Processing...
            </>
          ) : 'Buy'}
        </button>
      </div>
    </div>
  );
}

export default BicycleCard;