# Analysis of Variance (ANOVA) Test (for comparing more than two groups): (normal data)
#=======================================================================================================
## step by step Anova Calculation :
import numpy as np
from scipy.stats import f
import pandas as pd
# Sample data
data = pd.read_csv('E:/ANOsampledata.csv')

overall_mean = data.mean().mean()
group_means = data.mean(axis=0)
print(f"group_means: {group_means}")
print(f"overall_mean: {overall_mean}")

# Between-Group Sum of Squares
SSB = np.sum(data.shape[0] * (group_means - overall_mean)**2)
print(f"Between-Group Sum of Squares (SSB): {SSB}")

# Replicate the group means to match the shape of the original DataFrame
group_means_matrix = np.tile(group_means.values, (data.shape[0], 1))
#  Within-Group Sum of Squares
SSW = np.sum((data.values - group_means_matrix)**2)
print(f"within-Group Sum of Squares (SSW): {SSW}")

# Degrees of Freedom
df_between = data.shape[1] - 1
df_within = data.size - data.shape[1]
print(f"degree of freedom (df_between): {df_between}")
print(f"degree of freedom (df_within): {df_within}")

#  Mean Squares
MSB = SSB / df_between
MSW = SSW / df_within

# F-statistic
F = MSB / MSW
# Compare F-statistic with Critical Value or P-value
p_value = 1 - f.cdf(F, df_between, df_within)

# Print results
print(f"F-statistic: {F}")
print(f"P-value: {p_value}")








