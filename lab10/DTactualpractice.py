import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.preprocessing import LabelEncoder

# -------------------------------------------------------
# STEP 1: CREATE SYNTHETIC DATASET
# -------------------------------------------------------
np.random.seed(42)
n = 300

data = pd.DataFrame({
    'income':            np.random.randint(20000, 150000, n),
    'employment_status': np.random.choice(['Employed', 'Unemployed', 'Self-Employed'], n),
    'credit_score':      np.random.randint(300, 850, n),
    'loan_amount':       np.random.randint(5000, 50000, n),
    'marital_status':    np.random.choice(['Single', 'Married', 'Divorced'], n),
    'loan_approved':     np.random.choice([0, 1], n)   # 0=rejected, 1=approved
})

# Add some missing values
data.loc[3, 'income'] = np.nan
data.loc[15, 'credit_score'] = np.nan

# -------------------------------------------------------
# STEP 2: HANDLE MISSING VALUES
# -------------------------------------------------------
data['income'].fillna(data['income'].mean(), inplace=True)
data['credit_score'].fillna(data['credit_score'].mean(), inplace=True)

# -------------------------------------------------------
# STEP 3: ENCODE categorical columns
# -------------------------------------------------------
le = LabelEncoder()
data['employment_status'] = le.fit_transform(data['employment_status'])
# Employed=0, Self-Employed=1, Unemployed=2 (alphabetical)

data['marital_status'] = le.fit_transform(data['marital_status'])
# Divorced=0, Married=1, Single=2

# -------------------------------------------------------
# STEP 4: FEATURE SELECTION (correlation)
# -------------------------------------------------------
print("Feature correlation with loan_approved:")
print(data.corr()['loan_approved'].sort_values(ascending=False))

# -------------------------------------------------------
# STEP 5: SPLIT
# -------------------------------------------------------
X = data.drop('loan_approved', axis=1)
y = data['loan_approved']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------------------------------
# STEP 6: TRAIN Decision Tree
# -------------------------------------------------------
DT = DecisionTreeClassifier(random_state=42)
DT.fit(X_train, y_train)

# -------------------------------------------------------
# STEP 7: EVALUATE
# -------------------------------------------------------
y_pred = DT.predict(X_test)

print(f"\nAccuracy:  {accuracy_score(y_test, y_pred)*100:.2f}%")
print(f"Precision: {precision_score(y_test, y_pred)*100:.2f}%")
print(f"Recall:    {recall_score(y_test, y_pred)*100:.2f}%")
print(f"F1-Score:  {f1_score(y_test, y_pred)*100:.2f}%")
print("\nFull Report:\n", classification_report(y_test, y_pred))

# -------------------------------------------------------
# STEP 8: PREDICT for NEW applicant
# -------------------------------------------------------
new_applicant = pd.DataFrame({
    'income':            [75000],
    'employment_status': [0],     # 0 = Employed
    'credit_score':      [720],
    'loan_amount':       [15000],
    'marital_status':    [1]      # 1 = Married
})

result = DT.predict(new_applicant)
print(f"\nLoan Decision: {'APPROVED' if result[0]==1 else 'REJECTED'}")
