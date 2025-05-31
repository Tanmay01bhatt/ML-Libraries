# Splitting the data into train, test, val :
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv(
    "https://gitlab.com/AnalyticsIndiaMagazine/practicedatasets/-/raw/main/bootcamp/decision_tree_classification/BankNoteAuthentication.csv"
)

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 2 steps:

# 1 = temp and test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2 = train and val
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42
)

print(X_train.shape, X_test.shape, X_val.shape)

# shuffling and stratificaiton is done easily using this.

# Manual slicing
# useful in time-series data
# or in custom cross validation

indices = np.random.permutation(len(X))
X_shuffle = X.iloc[indices]
y_shuffle = y.iloc[indices]

num_samples = len(X_shuffle)
train_end = int(0.6 * num_samples)
val_end = int(0.8 * num_samples)

X_train2 = X_shuffle[:train_end]
X_val2 = X_shuffle[train_end:val_end]
X_test2 = X_shuffle[val_end:]

print(X_train2.shape, X_test2.shape, X_val2.shape)
