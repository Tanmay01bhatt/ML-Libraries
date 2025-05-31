# Chi-Square Distribution
# use in null hypothesis distrbution

# params :
# df = degree of freedom

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.chisquare(df=3, size=1000)
sns.displot(x, kind="kde")
plt.show()
