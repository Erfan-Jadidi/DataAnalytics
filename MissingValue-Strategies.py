import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer


df = pd.read_csv("F:\DA\DA 08\DA 08\data.csv")

# imput = SimpleImputer(missing_values=11, strategy="mean")
# imput = SimpleImputer(missing_values=np.nan, strategy="median")
# imput = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
# imput = SimpleImputer(missing_values=np.nan, strategy="constant, fill_value=10)

# imput = KNNImputer(n_neighbors=5)
#
# print(imput.fit_transform(df))

print(df)


df.where(df["a"]<100, np.nan, inplace=True)
impute = SimpleImputer(missing_values=np.nan, strategy="mean")
print(impute.fit_transform(df))

# print(df)

