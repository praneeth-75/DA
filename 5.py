import matplotlib.pyplot as plt
import numpy as np
x=[60,55,50,56,30,70,40,35,80,80,75]
y=[65,40,35,75,63,80,35,20,80,60,60]
rng=np.random.RandomState(0)
colors=rng.rand(11)
sizes=1000*rng.rand(11)
plt.scatter(x,y,c=colors,s=sizes,alpha=0.3,marker='o')
plt.xlabel("Marks in Python")
plt.ylabel("Marks in Data Analytics")
plt.title('Correlation between marks in Python and Data Analytics')
plt.show()


line graph
x=[10,20,30,40,50]
y=[20,25,22,12,44]
plt.plot(x,y)
plt.title("Line Graph",color='green')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


bar graph
plt.bar(x,y,color='green', edgecolor='blue', linewidth=2)
plt.title("Bar Graph")
plt.show()

histogram
x1=[12,14,12,18,16,16,15]
plt.hist(x)
plt.title("Histogram")
plt.show()

bar graph
plt.bar(x,y,color='green', edgecolor='blue', linestyle="--")
plt.title("Bar Graph")
plt.show()

pie chart
names=['krishna','sai,'kumar']
marks=[23,21,24,22]
plt.pie(marks,labels=names)
plt.title("Student Data")
plt.show()

stackplot

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(2015,2022,1)
series1=[3,2,4,1,5,6,2]
series2=[4,2,5,1,3,2,7]
series3=[3,5,1,2,4,6,7]
y=np.vstack([series1,series2,series3])
fig,ax=plt.subplots()
cols=["green","blue","pink"]
ax.stackplot(x,y,labels=["G1","G2","G3"],colors=cols,alpha=0.9)
ax.legend(loc='upper center')
ax.set(xlim=(min(x),max(x)),xticks=x)
plt.show()

