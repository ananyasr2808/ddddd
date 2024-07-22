import pandas as pd
import matplotlib.pyplot as plt
iris=pd.read_csv("C:/ananay/iris.csv")
print("\n the size of the data for given dataset \n")
print(iris.shape)
print("\n scatter plot to compare petal length and width\n")
plt.scatter(iris['petal_length'],iris['petal_width'])
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.show()
print("\n check for missing values:\n")
print(iris.isnull().sum())
print("\\n summary of the dataset\n ")
print(iris.describe())
      
                                      
