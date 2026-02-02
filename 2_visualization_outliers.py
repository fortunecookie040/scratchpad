# %%
# Extreme behavior
# models are robust if changes to highest and lowest values 
# do not significantly impact our estimates 
# The mean is not rebust, the median is. 

# replace standard deviation with interquartile range (IQR)
# IQR is more robust than standard deviation
# IQR = 0.75 quantile - 0.25 quantile (50% of the observations)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('data/craiglist_cville_cars_long.csv')
df.head()
# %%
df["price"].describe()
# %%
sns.ecdfplot(df["price"])
# %%
np.quantile(df["price"], 0.75) - np.quantile(df["price"], 0.25)
# 7437 IQR as opposed to standard deviation of 8170
# %%
# to create a function 
x = df["price"]
def outlier_analyze(x):
    q75 = np.quantile(x, 0.75)
    q25 = np.quantile(x, 0.25)
    iqr = q75 - q25
# range for outlier limits
    uw = q75 + 1.5 * iqr # upperwhisker
    lw= q25 - 1.5 * iqr # lowerwhisker
    upper_outlier = (x > uw)
    lower_outlier = (x < lw)
    outlier = upper_outlier + lower_outlier
    winsorize = (
        upper_outlier * uw + # map upper outlier to upperwhisker bc upper_outlier is 0, 1
        lower_outlier * lw + 
        (1-outlier)*x  #if neither, keep original value
    )
    return outlier, winsorize
# %%
sns.boxplot(x = df["price"])
# %%
df.loc[upper_outlier, :]
# dataframe of outliers only
# %%
# 3 stategies for dealing with outliers
# 1. Remove the outliers
# 2. Winsorize: round the values outside the whiskers to the values of 
#       the nearest whisker
# 3. Transform: take log or inverse hyperbolic sine to squash the data
#       into a smaller interval

# %%
outlier_result, winsorize_result = outlier_analyze(x)
# %%
sns.scatterplot(x = x, y = winsorize_result)
# %%
sns.boxplot(x = winsorize_result)
# %%
# adds a kde plot on top of the boxplot
# fill = false means the area under the curve is not filled
sns.violinplot(x = x, fill = False, inner = "quartile")
# %%
# Try it myself
df2 = pd.read_csv('data/wages_hw.csv')
df2.head()
# %%
df2["avg_salary"].describe()
# %% 
sns.boxplot(x = df2["avg_salary"])
# %%
result1, result2 = outlier_analyze(df2["avg_salary"])
# %%
sns.scatterplot(x = df2["avg_salary"], y = result2)
# %%
