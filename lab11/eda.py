import pandas as pd
import numpy as np
import seaborn as sns
import  matplotlib.pyplot as plt

# 1. Load the Dataset

df = pd.read_csv('house_prices_practice.csv')

# 2. Basic Data Overview

print("*** Dataset Description *** ")
print(df['SalePrice'].describe())


# 3. Distribution of SalesPrice
plt.figure(figsize=(9,8))
sns.histplot(df['SalePrice'] , color = 'blue' , bins=100 , kde=True)
plt.title('Histogram of SalePrice')
plt.xlabel('SalePrice')
plt.ylabel('Frequency')
plt.show()


# 4. Extracting Numeric values
df_num = df.select_dtypes(['int64','float64'])
print(" *** Numeric values  ***")
print(df_num.head())


# 5. Visualizing Histo all numeric values
df_num.hist(figsize=(16,20), bins=50 , xlabelsize=8 , ylabelsize=8)
plt.suptitle('Histogram of Numeric Values')
plt.show()



# Identifying features that correlate strongly with SalePrice
df_num_corr = df_num.corr()['SalePrice'][:-1] # Exclude SalePrice itself
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)

print("\n--- Golden Features (High Correlation > 0.5) ---")
print(golden_features_list)

# 7. Visualizing Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df_num.corr(), annot=False, cmap='coolwarm')
plt.title("Correlation Matrix of Numerical Features")
plt.show()
