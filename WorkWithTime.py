from datetime import datetime, timedelta

import pandas as pd

dt = datetime.now()
print(dt)
print(dt - timedelta(minutes=7))

def minus_7(date_time):
    return date_time - timedelta(days=39, minutes=7)


test = [{"Time":datetime(2019,1,18,20,19,32)},
        {"Time":datetime(2024,2,16,9,17,42)},
        {"Time":datetime(2000,12,1,21,29,17)}]

df = pd.DataFrame(test)

# df["Time"].dt.minute = df["Time"].dt.minute - df["Field"]

df.info()
df["Time"] = df["Time"].apply(minus_7)
print(df)


