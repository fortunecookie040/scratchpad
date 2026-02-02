# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/craiglist_cville_cars_long.csv")
df.head()
# %%
sns.kdeplot(df["price"])
# %%
df["price"].describe()
# %%
sns.histplot(np.log(df["price"]), bins=50)
# %%
sns.ecdfplot(df["price"])
# pick any price and go to up the line. The y value is the proportion of what is below that price. 
# ecde is roughly the integral of the kde. 
# %%
# 50th percentile --> q = 0.5
np.quantile(df["price"], q = 0.5)
# %%
df.shape
# %%
