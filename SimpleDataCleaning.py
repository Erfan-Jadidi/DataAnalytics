import pandas as pd

X1 = [{"id":1 ,"name":"ali", "age":20},{"id":2 ,"name":"reza", "age":17},{"id":3 ,"name":"mohsen", "age":22}]
X2 = [{"id":1 ,"name":"ali", "age":20}, {"id":10 ,"name":"ahmad", "age":25}]


df1 = pd.DataFrame(X1)
df2 = pd.DataFrame(X2)

# print(df1)
# print(df2)

new_df = pd.concat([df1, df2], axis=1)


new_df.columns = list("abcdef")

new_df.reset_index(inplace=True)
print(new_df)
print(new_df.drop(columns=['index']))