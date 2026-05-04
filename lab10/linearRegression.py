import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# -------------------------------------------------------
# STEP 1: CREATE SYNTHETIC DATASET
# -------------------------------------------------------
np.random.seed(42)
n = 200

data = pd.DataFrame({
    'study_hours':    np.random.uniform(1, 10, n),
    'attendance':     np.random.uniform(50, 100, n),
    'previous_grade': np.random.uniform(40, 100, n),
    'participation':  np.random.choice(['Low', 'Medium', 'High'], n),  # categorical
    'internet_usage': np.random.uniform(1, 8, n),
    'final_score':    np.random.uniform(40, 100, n)
})

# Manually add some missing values to practice handling them
data.loc[5, 'attendance'] = np.nan
data.loc[10, 'study_hours'] = np.nan
data.loc[20, 'previous_grade'] = np.nan

# -------------------------------------------------------
# STEP 2: CLEAN DATA - handle missing values
# -------------------------------------------------------
# Fill missing numbers with the column mean (average)
data['attendance'].fillna(data['attendance'].mean(), inplace=True)
data['study_hours'].fillna(data['study_hours'].mean(), inplace=True)
data['previous_grade'].fillna(data['previous_grade'].mean(), inplace=True)

print("Missing values after cleaning:\n", data.isnull().sum())

# -------------------------------------------------------
# STEP 3: ENCODE categorical variable (participation)
# Low=0, Medium=1, High=2
# -------------------------------------------------------
le = LabelEncoder()
data['participation'] = le.fit_transform(data['participation'])
# Now participation column has numbers instead of words

# -------------------------------------------------------
# STEP 4: SPLIT into X (features) and y (target)
# -------------------------------------------------------
X = data.drop('final_score', axis=1)   # everything except final_score
y = data['final_score']                 # only final_score

# -------------------------------------------------------
# STEP 5: FEATURE IMPORTANCE (using correlation)
# -------------------------------------------------------
print("\nCorrelation of each feature with final_score:")
print(data.corr()['final_score'].sort_values(ascending=False))
# higher absolute value = more important feature

# -------------------------------------------------------
# STEP 6: TRAIN/TEST SPLIT
# -------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------------------------------
# STEP 7: TRAIN the model
# -------------------------------------------------------
LR = LinearRegression()
LR.fit(X_train, y_train)

# -------------------------------------------------------
# STEP 8: PREDICT and EVALUATE
# -------------------------------------------------------
y_pred = LR.predict(X_test)

mae  = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2   = r2_score(y_test, y_pred)

print(f"\nMAE  (avg error in marks): {mae:.2f}")
print(f"RMSE (penalizes big errors): {rmse:.2f}")
print(f"R2   (how well model fits): {r2*100:.2f}%")

# -------------------------------------------------------
# STEP 9: PREDICT for a NEW student
# -------------------------------------------------------
new_student = pd.DataFrame({
    'study_hours':    [7],
    'attendance':     [85],
    'previous_grade': [78],
    'participation':  [2],    # 2 = High (encoded)
    'internet_usage': [3]
})

predicted_score = LR.predict(new_student)
print(f"\nPredicted final score for new student: {predicted_score[0]:.2f}")
