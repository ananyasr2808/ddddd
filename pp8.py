import matplotlib.pyplot as m
import pandas as p
data=p.read_csv("C:/ananay/iris.csv")
mpg=data['mpg']
m.hist(mpg,bins='auto',color='g',edgecolor='c')
m.xlabel('miles per galon(mpg)');
m.label("frequency")
m.title("frequency distribitionog mpg")
m.show()
