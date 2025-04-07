import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Sample data
X = np.array([[800, 2], [1200, 3], [1500, 3], [1800, 4], [2000, 4], [2200, 5], [2400, 4], [2600, 5]])
y = np.array([150000, 200000, 250000, 300000, 320000, 360000, 380000, 400000])

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'house_price_model.pkl')