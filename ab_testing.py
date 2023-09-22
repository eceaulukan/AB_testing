
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_control = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")

df_test = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")



df_control.head()
df_control.shape
df.describe().T

df_test.head()
df_test.shape
df.describe().T



df = pd.concat([df_control, df_test], axis=0, ignore_index=True)



# H0: m1 == m2 (control ve test gruplarının satın alma ortalamaları aynıdır)
# H1: m1 != m2 (control ve test gruplarının satın alma ortalamaları farklıdır)


df_control["Purchase"].mean()   ### 550.89
df_test["Purchase"].mean()      ### 582.11




## Kontrol grubunun normallik varsayımı

# H0: m1 == m2 (Kontrol grubunun dağılımı normal dağılım ile aynıdır)
# H1: m1 != m2 (Kontrol grubunun dağılımı normal dağılım ile farklıdır)

test_stat, pvalue = shapiro(df_control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p = 0.58 > 0.05 olduğu için H0 kabul edilir


## Test grubunun normallik varsayımı

# H0: m1 == m2 (Test grubunun dağılımı normal dağılım ile aynıdır)
# H1: m1 != m2 (Test grubunun dağılımı normal dağılım ile farklıdır)

test_stat, pvalue = shapiro(df_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p = 0.15 > 0.05 olduğu için H0 kabul edilir

#### Varyans homojenliği

# H0: m1 == m2 (Varyans homojendir)
# H1: m1 != m2 (değildir)
test_stat, pvalue = levene((df_control["Purchase"]), (df_test["Purchase"]))
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p = 0.11 > 0.05 olduğu için H0 kabul edilir



test_stat, pvalue = ttest_ind(df_control["Purchase"],df_test["Purchase"],equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# test sonucu p = 0.34 > 0.05 olduğu için H0 kabul edilir yani control ve test satın alma ortalamaları aynıdır

