import pandas as pd
import numpy as np
dict={'First Score': [100,90, np.nan, 95,95], 'Second Score': [30,45,56, np.nan, 56],'Third score':[np.nan,40,80,98,98]}
df = pd.DataFrame(dict)
df

df1=pd.DataFrame(dict)
df1.isnull()

df2=pd.DataFrame(dict)
df2.notnull()  

df3=pd.DataFrame(dict)
df3.fillna()  

df4=pd.DataFrame(dict)
values={"First Score": 70, "Second Score": 48, "Third Score":36}
df4.fillna (value=values)

df5=pd.DataFrame(dict)
df5.fillna(method='pad')

df6.DataFrame(dict)
df6.fillna(method='bfill')

df7=df5.fillna(value=100)
df7

df9=pd.DataFrame(dict)
Mean_fill=df9['First Score']. fillna(df9['First Score'].mean()) 
print (Mean_fill)

df10=pd.DataFrame(dict)
Mean_fill=df10['First Score']. fillna(df10['First Score'].median())
print (Median_fill)

df11=pd.DataFrame(dict)
Mean_fill=df11['First Score']. fillna(df9['First Score'].mode().iloc[0)]
print (Mode_fill)

import pandas as pd
import numpy as np
dict={'First Score': [100,90, np.nan, 95,95], 'Second Score': [30,45,56, np.nan, 56],'Third score':[np.nan,40,80,98,98]}
df12= pd.DataFrame(dict)
df12.replace(to_replace=np.nan,value=-999)

import pandas as pd
import numpy as np
dict={'First Score': [100,90, np.nan, 95,95], 'Second Score': [30,45,56, np.nan, 56],'Third score':[np.nan,40,80,98,98]}
df14 = pd.DataFrame(dict)
df14

df14.dropna(how='any)

df13=pd.DataFrame(dict)
df13['First Score'].interpolate (method='linear')
df13['Second Score'].interpolate (method='quadratic')

