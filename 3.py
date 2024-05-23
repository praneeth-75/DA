import numpy as np
from matplotlib import pyplot as plt
data= [3,386,479,627,20,523,482,483,542,699,535,617,577,471,615,583,441,562,
527,433,541,585,704,443,569,430,331,511,440,579,341,545,615,548,439,556,
442,624,444]
data=sorted(data)
print("ORIGINAL DATA LIST\n",data) 

q1=np.percentile (data, 25)
q3=np.percentile (data,75)
print("Q1:\n",q1)
print("Q3:\n",q3)
IQR=q3-q1
lwr_bound=q1-(1.5*IQR)
upr_bound=q3+(1.5*IQR)
print("LB:\n",lwr_bound)
print("UB:\n",upr_bound)
outliers=[]
for i in data:
 if(i<lwr_bound or i>upr_bound):
 outliers.append(i)
print('OUTLIERS IN DATASET IS',outliers) 

a=np.array(data)
plt.hist(a,bins=[0, 100, 200, 300, 400, 500,600,700, 800])
plt.title("Histogram showing the outliers in the given data set")
plt.show() 

q1,q3=np.percentile(data, [25,75])
iqr=q3-q1
LB=q1-(1.5*iqr)
UB=q3+(1.5*iqr)
final_list=[]
for x in data:
 if (x>LB) and (x<UB):
 final_list.append(x)
print (final_list)

b=np.array(final_list)
plt.hist(b,bins=[0, 100, 200, 300, 400, 500,600,700,800])
plt.title("Histogram showing no outliers in the given data set")
plt.show() 

