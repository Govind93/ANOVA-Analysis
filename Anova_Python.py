#2. Analysis of Variance (ANOVA) Test (for comparing more than two groups): (normal data)
import numpy as np
group1= [89,89,88,78,78];
group2= [93,92,94,89,88];
group3= [89,88,89,93,90];
group4=[81,78,81,92,82];

mean1 = np.mean(group1)
sum1 = np.sum(group1)
Var1 = np.var(group1)

from scipy.stats import f_oneway
# Assuming 'group1', 'group2', and 'group3' are your three groups
statistic_F, p_value = f_oneway(group1, group2, group3, group4)
# Check the p-value to determine if there is a significant difference
if p_value < 0.05:
    print("There is a significant difference between groups.")
else:
    print("There is no significant difference between groups.")

print(f"F-statistic: {statistic_F}")
print(f"p-value: {p_value}")

#=======================================================================================================


## step by step Anova Calculation :
import numpy as np
from scipy.stats import f

# Sample data
#data = pd.read_csv('data.csv')
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









