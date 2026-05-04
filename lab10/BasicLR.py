import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Dummy data: study hours vs exam score
X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([35,45,50,55,65,70,75,80,85,95])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

LR = LinearRegression()
ModelLR = LR.fit(x_train, y_train)

PredictionLR = ModelLR.predict(x_test)
print("Predictions:", PredictionLR)

# R2 score
teachLR = r2_score(y_test, PredictionLR)
print("Testing Accuracy (R2 %):", teachLR * 100)

# RMSE
rmse = np.sqrt(mean_squared_error(y_test, PredictionLR))
print("RMSE:", rmse)

# See the line equation
print("Slope (B1):", LR.coef_[0])
print("Intercept (B0):", LR.intercept_)
