import pandas as pd

from datetime import datetime,timedelta

if "ساعت پیش" in date_time:
    date_time - timedelta(hour=170)
elif "دقیقه پیش" in date_time:
    date_time - timedelta(minute=170)

dt = datetime.now()
print(dt)
print(dt - timedelta(minutes=170))

df = pd.read_excel("F:\\DA\\DA 07\\DA 07\\news.xlsx")

# df["time"] = df["time"].str.replace("دقیقه پیش", "")
# df["time"] = df["time"].str.replace("-", "")
# df["time"] = df["time"].str.strip()
#
# df["time"] = pd.to_numeric(df["time"])
#


def view_cleaner(view):
    if "K" in view:
        return int(float(view.replace("K", "")) * 1000)
    else:
        return int(view.replace("K", ""))

df["view_count"] = df["view"].apply(view_cleaner)
# df["view_count"] = df["view"].apply(lambda vw :float(vw.replace("K","")) * 1000 if "K" in vw else int(vw.replace("K","")))

# print(df)
df.info()
