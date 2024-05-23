import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('Fortune 500 2017 - Fortune 500.csv')
df.shape


df1=pd.DataFrame(df.head())
df1

df1.describe()

df1.describe(include=['object'])

df1.describe(include='all')
mean = df['Revenues'].mean()
print(mean)

median = df['Revenues'].median()
print(median)
mode = df['Revenues'].mode()
print(mode)

data = df['Revenues']
sns.distplot(data, bins=10, hist=True, kde=True, label = 'Revenue (in millions)')
df['Revenues'].min()
df['Revenues'].max()
df['Revenues'].max() - df['Revenues'].min()
df['Revenues'].var()
df['Revenues'].std()
Q2 = df['Revenues'].quantile(0.5)
Q2
Q3 = df['Revenues'].quantile(0.75)
Q3
Q1 = df['Revenues'].quantile(0.25)
Q1
IQR = Q3  - Q1
IQR
plt.boxplot(df['Revenues'])
plt.show()
