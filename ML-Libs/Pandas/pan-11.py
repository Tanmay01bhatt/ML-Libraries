# Selecting Data from a Dataset/Dataframe for ML Processing

import pandas as pd

data = pd.read_csv(
    "https://gitlab.com/AnalyticsIndiaMagazine/practicedatasets/-/raw/main/bootcamp/decision_tree_classification/BankNoteAuthentication.csv"
)

print(data.head())

# using drop():

X = data.drop("class", axis=1)
y = data["class"]

# using iloc[] :  data.iloc[rows,cols]

X1 = data.iloc[:, :-1]  # select all rows : select all cols except last one
y1 = data.iloc[:, -1]  # select all rows : select only the last col

# if we want to exclude the first col and start selecting from 2nd col : (start from skewness not variance)

X2 = data.iloc[:, 1:-1].values  # nd array = better to use
y2 = data.iloc[:, -1]  # pd.Series

print(X2)


# Further split into train,test sets :

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(X_train.shape, y_train.shape)
