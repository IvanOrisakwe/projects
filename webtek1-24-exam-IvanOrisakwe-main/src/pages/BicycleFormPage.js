import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import BicycleService from '../services/BicycleService';

function BicycleFormPage() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    brand: '',
    model: '',
    price: '',
    additionalInfo: '',
    imageUrl: 'https://via.placeholder.com/300x200?text=Bicycle+Image'
  });
  
  const [errors, setErrors] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
    
    if (errors[name]) {
      setErrors({ ...errors, [name]: null });
    }
  };

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.brand.trim()) {
      newErrors.brand = 'Brand is required';
    }
    
    if (!formData.model.trim()) {
      newErrors.model = 'Model is required';
    }
    
    if (!formData.price) {
      newErrors.price = 'Price is required';
    } else if (isNaN(Number(formData.price)) || Number(formData.price) <= 0) {
      newErrors.price = 'Price must be a positive number';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (validateForm()) {
      try {
        setSubmitting(true);
        setSubmitError(null);
        
        const bicycleData = {
          ...formData,
          price: Number(formData.price)
        };
        
        await BicycleService.addBicycle(bicycleData);
        alert('Bicycle sale announcement saved successfully!');
        navigate('/');
      } catch (error) {
        setSubmitError('Failed to save bicycle. Please try again.');
        console.error('Error saving bicycle:', error);
      } finally {
        setSubmitting(false);
      }
    }
  };

  return (
    <div>
      <h2>Add Bicycle for Sale</h2>
      
      {submitError && (
        <div className="alert alert-danger mb-3" role="alert">
          {submitError}
        </div>
      )}
      
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="brand" className="form-label">Brand *</label>
          <input
            type="text"
            className={`form-control ${errors.brand ? 'is-invalid' : ''}`}
            id="brand"
            name="brand"
            value={formData.brand}
            onChange={handleChange}
          />
          {errors.brand && <div className="invalid-feedback">{errors.brand}</div>}
        </div>
        
        <div className="mb-3">
          <label htmlFor="model" className="form-label">Model *</label>
          <input
            type="text"
            className={`form-control ${errors.model ? 'is-invalid' : ''}`}
            id="model"
            name="model"
            value={formData.model}
            onChange={handleChange}
          />
          {errors.model && <div className="invalid-feedback">{errors.model}</div>}
        </div>
        
        <div className="mb-3">
          <label htmlFor="price" className="form-label">Price ($) *</label>
          <input
            type="number"
            className={`form-control ${errors.price ? 'is-invalid' : ''}`}
            id="price"
            name="price"
            value={formData.price}
            onChange={handleChange}
          />
          {errors.price && <div className="invalid-feedback">{errors.price}</div>}
        </div>
        
        <div className="mb-3">
          <label htmlFor="imageUrl" className="form-label">Image URL</label>
          <input
            type="text"
            className="form-control"
            id="imageUrl"
            name="imageUrl"
            value={formData.imageUrl}
            onChange={handleChange}
          />
          <div className="form-text">Enter a URL for the bicycle image (optional)</div>
        </div>
        
        <div className="mb-3">
          <label htmlFor="additionalInfo" className="form-label">Additional Information</label>
          <textarea
            className="form-control"
            id="additionalInfo"
            name="additionalInfo"
            rows="3"
            value={formData.additionalInfo}
            onChange={handleChange}
          ></textarea>
        </div>
        
        <button 
          type="submit" 
          className="btn btn-primary"
          disabled={submitting}
        >
          {submitting ? (
            <>
              <span className="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
              Saving...
            </>
          ) : 'Save'}
        </button>
      </form>
    </div>
  );
}

export default BicycleFormPage;