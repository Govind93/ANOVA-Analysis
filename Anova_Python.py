# Analysis of Variance (ANOVA) Test (for comparing more than two groups): (normal data)
#=======================================================================================================
## step by step Anova Calculation :
import numpy as np
from scipy.stats import f

# Sample data 
## data = pd.read_csv('data.csv') # instead of Array we can read our CSV file.
data = np.array([[89,89,88,78,78], [93,92,94,89,88], [89,88,89,93,90], [81,78,81,92,82]])

# Step 1: Calculate overall mean
overall_mean = np.mean(data)

# Step 2: Calculate group means
group_means = np.mean(data, axis=1)

# Step 3: Calculate Between-Group Sum of Squares (SSB)
SSB = np.sum(data.shape[1] * (group_means - overall_mean)**2)

# Step 4: Calculate Within-Group Sum of Squares (SSW)
SSW = np.sum((data - group_means[:, np.newaxis])**2)

# Step 5: Calculate Degrees of Freedom
df_between = data.shape[0] - 1
df_within = data.size - data.shape[0]

# Step 6: Calculate Mean Squares
MSB = SSB / df_between
MSW = SSW / df_within

# Step 7: Calculate F-statistic
F = MSB / MSW

# Step 8: Compare F-statistic with Critical Value or P-value
p_value = 1 - f.cdf(F, df_between, df_within)

# Print results
print(f"F-statistic: {F}")
print(f"P-value: {p_value}")









