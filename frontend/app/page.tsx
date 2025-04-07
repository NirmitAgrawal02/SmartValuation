"use client";

import { useState } from 'react';

export default function Home() {
  const [sqft, setSqft] = useState('');
  const [bedrooms, setBedrooms] = useState('');
  const [modelType, setModelType] = useState('linear');
  const [predictedPrice, setPredictedPrice] = useState<number | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        sqft: parseFloat(sqft),
        bedrooms: parseInt(bedrooms),
        model_type: modelType,
      }),
    });
    const data = await response.json();
    setPredictedPrice(data.predicted_price);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg max-w-md w-full">
        <h1 className="text-2xl font-bold mb-6 text-center">House Price Prediction</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Square Footage
              <input
                type="number"
                value={sqft}
                onChange={(e) => setSqft(e.target.value)}
                className="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </label>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Number of Bedrooms
              <input
                type="number"
                value={bedrooms}
                onChange={(e) => setBedrooms(e.target.value)}
                className="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </label>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Model Type
              <select
                value={modelType}
                onChange={(e) => setModelType(e.target.value)}
                className="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="linear">Linear Regression</option>
                <option value="random_forest">Random Forest</option>
                <option value="svr">Support Vector Regression</option>
              </select>
            </label>
          </div>
          <button
            type="submit"
            className="w-full bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 transition"
          >
            Predict Price
          </button>
        </form>
        {predictedPrice !== null && (
          <p className="mt-4 text-center text-lg font-semibold">
            Predicted Price: ${predictedPrice.toLocaleString()}
          </p>
        )}
      </div>
    </div>
  );
}