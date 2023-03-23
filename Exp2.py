import pandas as pd
df = pd.read_csv('bhp.csv')

#Remove outliers using IQR
Q1 = df['price_per_sqft'].quantile(0.25)
Q3 = df['price_per_sqft'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR
df_iqr = df[(df['price_per_sqft'] >= lower_limit) & (df['price_per_sqft'] <= upper_limit)]
print(df_iqr)

# Use zscore of 3 to remove outliers
from scipy.stats import zscore
df_z = df_iqr[(zscore(df_iqr['price_per_sqft']) < 3)]
print(df_z)

#(4) for the data set height_weight.csv find the following
# (i) Using IQR detect weight outliers and print them

data = pd.read_csv('height_weight.csv')
# Display the first few rows of the data to make sure it was loaded correctly
print(data.head())

# Calculate the IQR for the weight column
Q1 = data['weight'].quantile(0.25)
Q3 = data['weight'].quantile(0.75)
IQR = Q3 - Q1

# Calculate the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find the outliers
outliers = data[(data['weight'] < lower_bound) | (data['weight'] > upper_bound)]
print(outliers)
print('\n')

#(ii) Using IQR, detect height outliers and print them

# Calculate the IQR for the height column
Q1 = data['height'].quantile(0.25)
Q3 = data['height'].quantile(0.75)
IQR = Q3 - Q1

# Calculate the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find the outliers
outliers = data[(data['height'] < lower_bound) | (data['height'] > upper_bound)]
print(outliers)
