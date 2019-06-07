import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.datasets import load_boston
boston = load_boston()
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names

correlation_matrix = bos.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()