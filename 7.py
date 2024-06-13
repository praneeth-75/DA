#Step 2:
# Checking the normality using Shapiro test
import numpy as np
from scipy import stats
def check_normality(data):
        test_stat_normality, p_value_normality=stats.shapiro(data)
        print("p value:%.4f" % p_value_normality)
        if p_value_normality <0.05:
                print("Reject null hypothesis >> The data is not normally distributed")
        else:
            print("Fail to reject null hypothesis >> The data is normally distributed")

sync = np.array([94. , 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2,87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])
asyncr = np.array([77.1, 71.7, 91. , 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])
check_normality(sync)
check_normality(asyncr)
print("")
# Checking the variance Homogeneity using Levene's test
def check_variance_homogeneity(group1, group2):
    test_stat_var, p_value_var= stats.levene(group1,group2)
    print("p value:%.4f" % p_value_var)
    if p_value_var <0.05:
            print("Reject null hypothesis >> The variances of the samples are different.")
    else:
        print("Fail to reject null hypothesis >> The variances of the samples are same.")

check_variance_homogeneity(sync, asyncr)
print("")
#Step 3:
#Since assumptions are satisfied, we can perform the parametric version of the test for 2 groups and
# Used t-test as sample size is small and means of two groups can be compared and variances are know
ttest,p_value = stats.ttest_ind(sync, asyncr)
print("p value:%.8f" % p_value)
print("since the hypothesis is one sided >> use p_value/2 >> p_value_one_sided:%.4f" %(p_value/2))
if p_value/2 <0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")
