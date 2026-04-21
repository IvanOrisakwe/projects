
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import BicycleListPage from './pages/BicycleListPage';
import BicycleFormPage from './pages/BicycleFormPage';

function App() {
  return (
    <Router>
      <div className="container mt-4">
        <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
          <div className="container-fluid">
            <span className="navbar-brand">Bicycle Sales App</span>
            <div className="navbar-nav">
              <Link className="nav-link" to="/">View Bicycles</Link>
              <Link className="nav-link" to="/add">Add Bicycle</Link>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<BicycleListPage />} />
          <Route path="/add" element={<BicycleFormPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;