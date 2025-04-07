from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Load the pre-trained model
model = joblib.load('house_price_model.pkl')

# Database connection
def get_db_connection():
    conn = sqlite3.connect('predictions.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS predictions
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     sqft REAL,
                     bedrooms INTEGER,
                     predicted_price REAL)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sqft = data['sqft']
    bedrooms = data['bedrooms']
    
    # Predict the price
    predicted_price = model.predict([[sqft, bedrooms]])[0]
    
    # Store in database
    conn = get_db_connection()
    conn.execute('INSERT INTO predictions (sqft, bedrooms, predicted_price) VALUES (?, ?, ?)',
                 (sqft, bedrooms, predicted_price))
    conn.commit()
    conn.close()
    
    # Return the predicted price
    return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)