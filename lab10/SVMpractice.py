from ortools.sat.python import cp_model
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler

np.random.seed(42)
n = 300

data = pd.DataFrame({
    'monthly_charges' : np.random.uniform(20,120, n),
    'contract_type' : np.random.choice(['Month-to-month', 'One year', 'Two year'], n),
    'tenure': np.random.randint(1, 72, n),
    'internet_service': np.random.choice(['DSL', 'Fiber', 'No'], n),
    'support_calls': np.random.randint(0, 10, n),
    'churn': np.random.choice([0, 1], n)
})

Q1 = data['monthly_charges'].quantile(0.25)
Q3 = data['monthly_charges'].quantile(0.75)
IQR = Q3 - Q1
data['monthly_charges'] = data['monthly_charges'].clip(Q1-1.5*IQR, Q3 + 1.5*IQR)

le = LabelEncoder()
data['monthly_charges'] = le.fit_transform(data['monthly_charges'])
data['internet_service'] = le.fit_transform(data['internet_service'])

X = data.drop(['churn'], axis=1)
Y = data['churn']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(X_train, Y_train)

y_pred = svm.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred))
print("\nAccuracy:", accuracy_score(Y_test, y_pred) * 100, "%")
print("\nFull Report:\n", classification_report(Y_test, y_pred))

new_customer = pd.DataFrame({
    'monthly_charges':  [95.0],
    'contract_type':    [0],
    'tenure':           [5],
    'internet_service': [1],
    'support_calls':    [7]
})

new_customer = scaler.transform(new_customer)
result = svm.predict(new_customer)
print("\nChurn Prediction:", "WILL CHURN" if result[0] == 1 else "WILL STAY")
