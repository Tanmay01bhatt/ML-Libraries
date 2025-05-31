# Correlation
# 1 = high corr = directly proportional
# 0 = No corr = no relationhip
# -1 = negative corr = inversely proportional

import pandas as pd

data = pd.read_csv(
    "https://raw.githubusercontent.com/analyticsindiamagazine/MocksDatasets/main/Customer_Missing.csv"
)

data.fillna(method="ffill", inplace=True)
print(data.isnull().sum())

data.drop(["Cust_City", "S.No."], axis=1, inplace=True)

# of whole dataset
print(data.corr(method="pearson", min_periods=1))

# 1 col with another

print(data["Cust_Age"].corr(data["Cust_Month_Income"]))

# ONLY WORKS ON NUMERICAL VALUES

# covariance = not standardized rande = (-infinity,+infinity)

print(data.cov(min_periods=None, ddof=1))

# Revise Stats Notes
