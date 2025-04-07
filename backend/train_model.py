import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import joblib

# Sample data
X = np.array([[800, 2], [1200, 3], [1500, 3], [1800, 4], [2000, 4], [2200, 5], [2400, 4], [2600, 5]])
y = np.array([150000, 200000, 250000, 300000, 320000, 360000, 380000, 400000])

# Train Linear Regression
lr_model = LinearRegression()
lr_model.fit(X, y)
joblib.dump(lr_model, 'lr_model.pkl')

# Train Random Forest Regression
rf_model = RandomForestRegressor(n_estimators=50, random_state=42)  # Reduced n_estimators for small data
rf_model.fit(X, y)
joblib.dump(rf_model, 'rf_model.pkl')

# Train SVR with RBF kernel
svr_model = SVR(kernel='rbf', C=100000, gamma='scale')  # Tuned for small dataset
svr_model.fit(X, y)
joblib.dump(svr_model, 'svr_model.pkl')