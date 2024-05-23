import pandas as pd
import numpy as np
from sklearn import preprocessing
import scipy.stats as s
d={'C1':[1,3,7,4], 'C2':[12,2,7,1], 'C3': [22,34,-11,9]}
df2=pd.DataFrame(d)
print("\n ORIGINAL DATA VALUES")
print("-----------------------")
print(df2) 

print("\n\n Data scaled between 0 and 1")
data_scaler=preprocessing.MinMaxScaler (feature_range=(0,1))
data_scaled=data_scaler.fit_transform(df2)
print("\nMin Max Scaled Data")
print("---------------------")
print(data_scaled.round(2)) 

dn=preprocessing.normalize (df2, norm='l1')
print("\n L1 Normalized data")
print("---------------------")
print(dn.round(2))

data_binarized=preprocessing.Binarizer(threshold=5).transform(df2)
print("\n Binarizing the data into os with value <=5 and into 1s with value
print("--------------------------------------------------------------------
print(data_binarized)

X_train=np.array([[1.,-1.,2.], [2.,0.,0.], [0.,1., -1]])
print("Original Data \n", X_train)
print("\nInitial mean:",s.tmean (X_train).round(2))
print("\n Initial Standard Deviation:",round(X_train.std(),2))
X_scaled=preprocessing.scale(X_train)
X_scaled.mean(axis=0)
X_scaled.std(axis=0)
print("\n\nStandardized Data \n", X_scaled.round(2))
print("\nScaled mean:",s.tmean (X_scaled).round(2))
print("\n Scaled Standard Deviation:",round(X_scaled.std(),2)) 

