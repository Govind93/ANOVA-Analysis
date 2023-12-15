Introduction:
ANOVA is a statistical technique that is used for analyzing the differences in means in three or more independent groups. It compares the variance between-groups means
to the variance within-groups. However, ANOVA is conducted using the same five step approach. 

ANOVA Hypotheses
•	Null hypothesis: Groups means are equal (no variation in means of groups)
H0: μ1=μ2=…=μp
•	Alternative hypothesis: At least, one group mean is different from other groups
H1: All μ are not equal
Null hypothesis is tested using the F-test for all groups.

Objectives:
1.	Perform analysis of variance by hand
2.	Interpret results of analysis of variance tests
3.	Identify the hypothesis testing procedure based on type of outcome variable and number of samples


Data Results:

print(f"F-statistic: {F}")
print(f"P-value: {p_value}")
group_means: 
p1    84.4
p2    91.2
p3    89.8
p4    82.8
dtype: float64
overall_mean: 87.05000000000001
Between-Group Sum of Squares (SSB): 249.35
within-Group Sum of Squares (SSW): 293.59999999999997
degree of freedom (df_between): 3
degree of freedom (df_within): 16
F-statistic: 4.52951
P-value: 0.017566

 Conclusion:
We reject H0 because [f cal > f tab]: 4.52 > 3.23. We have statistically significant evidence at α=0.05 to show that there is a difference in mean between the four groups. Hence, observed value of F is greater than the value in the F table value, then we can reject the null hypothesis with 95 percent confidence.


