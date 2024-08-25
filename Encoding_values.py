from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder

result = ["football", "tennis", "volleyball", "tennis", "tennis", "football", "football", "football", "volleyball"]

encoder = LabelEncoder()
encoder.fit(result)

t_result = encoder.transform(result)

print(t_result)
print(encoder.inverse_transform([0]))
# this help us to use string as number so that we can play with it :)