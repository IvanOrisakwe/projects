
const API_URL = 'http://localhost:5000/api';

class BicycleService {
  async getAllBicycles() {
    try {
      const response = await fetch(`${API_URL}/bicycles`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return await response.json();
    } catch (error) {
      console.error('Error fetching bicycles:', error);
      return [];
    }
  }

  async addBicycle(bicycle) {
    try {
      const response = await fetch(`${API_URL}/bicycles`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          brand: bicycle.brand,
          model: bicycle.model,
          price: bicycle.price,
          additionalInfo: bicycle.additionalInfo,
          imageUrl: bicycle.imageUrl
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return await response.json();
    } catch (error) {
      console.error('Error adding bicycle:', error);
      throw error;
    }
  }

  async deleteBicycle(id) {
    try {
      const response = await fetch(`${API_URL}/bicycles/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return true;
    } catch (error) {
      console.error('Error deleting bicycle:', error);
      return false;
    }
  }
}

export default new BicycleService();