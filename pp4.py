import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
da={'n':[1,2,3,4,5],'pencil':[300,350,400,500,520],'textbook':[250,350,400,420,500],'drawing sheets':[100,200,300,200,500],'total':[800,1380,2000,1400,2000],
    'profits':[8000,9500,10256,12000,18000]}
df=pd.DataFrame(da)
print(df)
sta=df.describe()
print("\n statistics of the dataset:\n",sta)
su=df['profits'].sum()
print("\n sum of profits:\n",su)
mi=df.isna()
print("\n missing values:\n",mi)
print("\n maximum value:\n",df['drawing sheets'].max())
plt.plot(df['n'],df['profits'],'^-',color='k')
plt.xlabel("numbers")
plt.ylabel("profits")
plt.show()
