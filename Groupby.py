import yfinance as yf

df = yf.download("BTC-USD")

df.info()

df["Date"] = df.index
df["WeekDay"] = df["Date"].dt.weekday
df.drop(columns="Date", inplace=True)

print(df.groupby("WeekDay").value_counts())
print(df.groupby("WeekDay").min())
print(df.groupby("WeekDay").sum())
print(df.groupby("WeekDay").mean())
print(df.groupby("WeekDay").idxmax())
print(df.groupby("WeekDay").idxmin())
