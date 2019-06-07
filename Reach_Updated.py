import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
from matplotlib import pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
import seaborn as sns

iris = sns.load_dataset("iris")
g = sns.pairplot(iris)
g = sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
g = sns.pairplot(iris, kind="reg")
g = sns.pairplot(iris, kind="reg", hue="species", diag_kind='kde')
plt.show()