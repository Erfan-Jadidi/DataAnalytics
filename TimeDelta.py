import re
from datetime import datetime, timedelta

import pandas as pd

# text = "17 دقیقه پیش"
#
# num = int(re.findall(r"\d+", text)[0])
#
# if  "دقیقه" in text:
#         print(num)
# elif  "ساعت" in text:
#         print(num * 60)



test = [{"past":1},
        {"past":12},
        {"past":13}]

df = pd.DataFrame(test)


df["time"] = df["past"].apply(lambda p:datetime.now() - timedelta(minutes=p))

print(df)

