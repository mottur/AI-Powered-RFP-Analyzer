import React, { useState, useEffect } from 'react';
import { apiService } from '../services/api';

const Categories = () => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchItems = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await apiService.getItems();
      setItems(data.items || []);
    } catch (err) {
      setError('Failed to fetch items. Make sure the FastAPI server is running.');
      console.error('API Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateItem = async () => {
    try {
      const newItem = { 
        name: `Item ${Date.now()}`,
        description: `Description for item ${Date.now()}`
      };
      await apiService.createItem(newItem);
      fetchItems(); // Refresh the list
    } catch (err) {
      setError('Failed to create item');
      console.error('Error:', err);
    }
  };

  useEffect(() => {
    fetchItems();
  }, []);

  if (loading) return <div className="loading">Loading items...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="item-list">
      <h2>Items from FastAPI</h2>
      <button onClick={handleCreateItem} className="btn-primary">
        Add New Item
      </button>
      
      <div className="items-container">
        {items.length === 0 ? (
          <p>No items found</p>
        ) : (
          items.map((item, index) => (
            <div key={index} className="item-card">
              <h3>{item}</h3>
              <p>ID: {index + 1}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Categories;