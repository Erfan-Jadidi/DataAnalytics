from matplotlib import pyplot as plt
from sklearn.datasets import load_diabetes
import seaborn as sns

X,y  = load_diabetes(as_frame=True,return_X_y=True)

# 
X["diabetes"] = y


sns.heatmap(X.corr(), cmap="coolwarm", annot=True, fmt=".4f")
plt.show()
# this project help us to find relations between diabetes values that helps doctors to find a better way.