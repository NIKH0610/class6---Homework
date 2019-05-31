import pandas as pd
import numpy as np
import sklearn
import seaborn as sns

from sklearn.datasets import load_boston
boston = load_boston()
bos = pn.DataFrame(boston.data)
bos.columns = boston.feature_names

for i in range(50):
    a = 0;
    b = 0;
    while (a==b):
        a = np.random.randit(low = 1, high = 13)
        b = np.random.randit(low = 1, high = 13)
    feature1 = boston.feature_names[a]
    feature2 = boston.feature_names[b]
    print(feature1);
    print(feature2);