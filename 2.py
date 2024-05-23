import pandas as pd
import numpy as np
df=pd.DataFrame({'Fast_Food': ['pizza', 'burger', 'momos', 'noodles', 'sandwich','pasta','macaroni','french_fries','gobi'], 'Price': [350, 200, 120, 160, 150, 300, 270, 100,70]})
print("\n ORIGINAL DATASET")
print(df)

m1=min (df["Price"])
 m2=max(df["Price"])
bins=np.linspace (m1,m2,4)
names=["Low", "Medium", "High"]
df["Price_bin"]=pd.cut (df["Price"],bins, labels=names,include_lowest=True)
print("\n BINNED DATASET")
print(df)
print(df.Price_bin.value_counts())

from matplotlib import pyplot as plt
a=np.array(df)
plt.hist(a,bins=np.linspace(min(df['Price']),max(df['Price']),4))
plt.axis([m1, m2,0,5])
plt.xlabel('Price Range: Low, Medium,High')
plt.ylabel('No. of Items')
plt.title("Histogram of Price of items")
plt.show()
