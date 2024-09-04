import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

df = pd.read_csv("F:\DA\DA 06\DA 06\Mall_Customers.csv")

df.drop(columns="CustomerID", inplace=True)

encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])

print(encoder.inverse_transform([0]))
print(encoder.inverse_transform([1]))
# df.info()
# print(df)

sns.pairplot(df, hue="Spending")
plt.show()