import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -------------------------------------------------------
# STEP 1: LOAD DATA
# -------------------------------------------------------
data = pd.read_csv('customer_churn.csv')

print("=== Raw Data ===")
print(data.head())
print("\nShape:", data.shape)
print("\nMissing values:\n", data.isnull().sum())
print("\nChurn distribution:\n", data['Churn'].value_counts())

# -------------------------------------------------------
# STEP 2: DROP useless column
# -------------------------------------------------------
data.drop('CustomerID', axis=1, inplace=True)
# CustomerID is just a serial number, has no effect on churn

# -------------------------------------------------------
# STEP 3: HANDLE MISSING VALUES
# -------------------------------------------------------
# Numeric columns → fill with mean
data['Tenure'].fillna(data['Tenure'].mean(), inplace=True)
data['MonthlyCharges'].fillna(data['MonthlyCharges'].mean(), inplace=True)
data['SupportCalls'].fillna(data['SupportCalls'].mean(), inplace=True)

# Categorical column → fill with most frequent value (mode)
data['ContractType'].fillna(data['ContractType'].mode()[0], inplace=True)

print("\nMissing values after cleaning:\n", data.isnull().sum())

# -------------------------------------------------------
# STEP 4: ENCODE categorical columns
# -------------------------------------------------------
le = LabelEncoder()
data['Gender']       = le.fit_transform(data['Gender'])
# Female=0, Male=1

data['ContractType'] = le.fit_transform(data['ContractType'])
# Monthly=0, Yearly=1

print("\nData after encoding:\n", data.head())

# -------------------------------------------------------
# STEP 5: HANDLE OUTLIERS on MonthlyCharges
# -------------------------------------------------------
Q1  = data['MonthlyCharges'].quantile(0.25)
Q3  = data['MonthlyCharges'].quantile(0.75)
IQR = Q3 - Q1
data['MonthlyCharges'] = data['MonthlyCharges'].clip(Q1 - 1.5*IQR, Q3 + 1.5*IQR)

# -------------------------------------------------------
# STEP 6: SPLIT X and y
# -------------------------------------------------------
X = data.drop('Churn', axis=1)   # all columns except Churn
y = data['Churn']                 # only Churn column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining samples: {len(X_train)}, Testing samples: {len(X_test)}")

# -------------------------------------------------------
# STEP 7: FEATURE SCALING (required for SVM)
# -------------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
# Note: Decision Tree doesn't need scaling but we'll use scaled data for both
# so the comparison is fair

# -------------------------------------------------------
# STEP 8: TRAIN MODEL 1 — SVM
# -------------------------------------------------------
svm = SVC(kernel='rbf', C=1, gamma='scale', random_state=42)
svm.fit(X_train_scaled, y_train)

svm_train_pred = svm.predict(X_train_scaled)
svm_test_pred  = svm.predict(X_test_scaled)

svm_train_acc = accuracy_score(y_train, svm_train_pred) * 100
svm_test_acc  = accuracy_score(y_test,  svm_test_pred)  * 100

# -------------------------------------------------------
# STEP 9: TRAIN MODEL 2 — Decision Tree
# -------------------------------------------------------
# max_depth=3 limits tree depth → prevents overfitting
DT = DecisionTreeClassifier(random_state=42, max_depth=3)
DT.fit(X_train_scaled, y_train)

dt_train_pred = DT.predict(X_train_scaled)
dt_test_pred  = DT.predict(X_test_scaled)

dt_train_acc = accuracy_score(y_train, dt_train_pred) * 100
dt_test_acc  = accuracy_score(y_test,  dt_test_pred)  * 100

# -------------------------------------------------------
# STEP 10: COMPARE RESULTS
# -------------------------------------------------------
print("\n============================================")
print("         MODEL PERFORMANCE COMPARISON       ")
print("============================================")
print(f"{'Model':<20} {'Train Acc':>10} {'Test Acc':>10}")
print(f"{'-'*42}")
print(f"{'SVM':<20} {svm_train_acc:>9.2f}% {svm_test_acc:>9.2f}%")
print(f"{'Decision Tree':<20} {dt_train_acc:>9.2f}% {dt_test_acc:>9.2f}%")
print("============================================")

# -------------------------------------------------------
# STEP 11: DETAILED REPORT for both models
# -------------------------------------------------------
print("\n=== SVM Confusion Matrix ===")
print(confusion_matrix(y_test, svm_test_pred))
print("\n=== SVM Classification Report ===")
print(classification_report(y_test, svm_test_pred))

print("\n=== Decision Tree Confusion Matrix ===")
print(confusion_matrix(y_test, dt_test_pred))
print("\n=== Decision Tree Classification Report ===")
print(classification_report(y_test, dt_test_pred))

# -------------------------------------------------------
# STEP 12: OVERFITTING CHECK + FINAL VERDICT
# -------------------------------------------------------
print("\n=== Overfitting Check ===")
svm_gap = svm_train_acc - svm_test_acc
dt_gap  = dt_train_acc  - dt_test_acc

print(f"SVM gap (train-test):           {svm_gap:.2f}%")
print(f"Decision Tree gap (train-test): {dt_gap:.2f}%")
print("(gap > 10% usually means overfitting)")

print("\n=== Final Verdict ===")
if svm_test_acc > dt_test_acc:
    print("SVM performs better on unseen data → recommended model")
else:
    print("Decision Tree performs better on unseen data → recommended model")

# -------------------------------------------------------
# STEP 13: PREDICT for a new customer
# -------------------------------------------------------
new_customer = pd.DataFrame({
    'Gender':          [1],    # 1 = Male
    'Tenure':          [5],    # only 5 months
    'MonthlyCharges':  [300],
    'ContractType':    [0],    # 0 = Monthly
    'SupportCalls':    [6]     # calls a lot = unhappy
})

new_scaled = scaler.transform(new_customer)

svm_result = svm.predict(new_scaled)
dt_result  = DT.predict(new_scaled)

print("\n=== New Customer Prediction ===")
print(f"SVM says:           {'WILL CHURN' if svm_result[0]==1 else 'WILL STAY'}")
print(f"Decision Tree says: {'WILL CHURN' if dt_result[0]==1 else 'WILL STAY'}")
