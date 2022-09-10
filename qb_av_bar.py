import pandas as pd
import matplotlib.pyplot as plt

av = [316, 216, 192, 211]
rate = [97.6, 86.4, 92.3, 78.2]
index = ['TB', 'DM', 'JM', 'JU']

df = pd.DataFrame({'av': av, 'rate': rate}, index=index)
ax = df.plot.bar(rot=0)

plt.show()
