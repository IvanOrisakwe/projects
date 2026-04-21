
const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const port = 5000;


app.use(cors());
app.use(bodyParser.json());


const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',   
  password: '',   
  database: 'bicycle_sales'
});


db.connect(err => {
  if (err) {
    console.error('Error connecting to MySQL:', err);
    return;
  }
  console.log('Connected to MySQL database');
  

  const createTableQuery = `
    CREATE TABLE IF NOT EXISTS bicycles (
      id INT AUTO_INCREMENT PRIMARY KEY,
      brand VARCHAR(100) NOT NULL,
      model VARCHAR(100) NOT NULL,
      price DECIMAL(10, 2) NOT NULL,
      additional_info TEXT,
      image_url TEXT,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
  `;
  
  db.query(createTableQuery, (err) => {
    if (err) {
      console.error('Error creating table:', err);
    } else {
      console.log('Bicycles table ready');
    }
  });
});




app.get('/api/bicycles', (req, res) => {
  db.query('SELECT * FROM bicycles ORDER BY created_at DESC', (err, results) => {
    if (err) {
      console.error('Error fetching bicycles:', err);
      return res.status(500).json({ error: 'Error fetching data' });
    }
    res.json(results);
  });
});


app.post('/api/bicycles', (req, res) => {
  const { brand, model, price, additionalInfo, imageUrl } = req.body;
  
  if (!brand || !model || !price) {
    return res.status(400).json({ error: 'Brand, model, and price are required' });
  }
  
  const query = `
    INSERT INTO bicycles (brand, model, price, additional_info, image_url)
    VALUES (?, ?, ?, ?, ?)
  `;
  
  db.query(
    query,
    [brand, model, price, additionalInfo, imageUrl],
    (err, result) => {
      if (err) {
        console.error('Error adding bicycle:', err);
        return res.status(500).json({ error: 'Error saving data' });
      }
      
      db.query('SELECT * FROM bicycles WHERE id = ?', [result.insertId], (err, rows) => {
        if (err) {
          return res.status(201).json({ id: result.insertId, message: 'Bicycle added successfully' });
        }
        res.status(201).json(rows[0]);
      });
    }
  );
});


app.delete('/api/bicycles/:id', (req, res) => {
  const id = req.params.id;
  
  db.query('DELETE FROM bicycles WHERE id = ?', [id], (err, result) => {
    if (err) {
      console.error('Error deleting bicycle:', err);
      return res.status(500).json({ error: 'Error deleting data' });
    }
    
    if (result.affectedRows === 0) {
      return res.status(404).json({ error: 'Bicycle not found' });
    }
    
    res.json({ message: 'Bicycle deleted successfully' });
  });
});


app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});