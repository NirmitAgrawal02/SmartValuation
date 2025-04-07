from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import sqlite3

app = Flask(__name__)
CORS(app)

# Load pre-trained models
models = {
    'linear': joblib.load('lr_model.pkl'),
    'random_forest': joblib.load('rf_model.pkl'),
    'svr': joblib.load('svr_model.pkl')
}

# Database setup
def get_db_connection():
    conn = sqlite3.connect('predictions.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS predictions
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     sqft REAL,
                     bedrooms INTEGER,
                     model_type TEXT,
                     predicted_price REAL)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sqft = data['sqft']
    bedrooms = data['bedrooms']
    model_type = data['model_type']  # 'linear', 'random_forest', or 'svr'

    # Select model
    if model_type not in models:
        return jsonify({'error': 'Invalid model type'}), 400
    model = models[model_type]
    predicted_price = model.predict([[sqft, bedrooms]])[0]

    # Store in database
    conn = get_db_connection()
    conn.execute('INSERT INTO predictions (sqft, bedrooms, model_type, predicted_price) VALUES (?, ?, ?, ?)',
                 (sqft, bedrooms, model_type, predicted_price))
    conn.commit()
    conn.close()

    return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)