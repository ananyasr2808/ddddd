import pandas as p
import matplotlib.pyplot as m
d={"firstname":["aryan","rohan","thanu","manu","siddhanth"],
   "lastname":["singh","aragrwal","raj","deep","nigam"],
   "type":["fulltime","itern","fulltime","parttime","itern"],
   "dept":["administration","technical","administration","technical","mangement"],
   "yoe":[2,3,4,5,6],"salary":[20000,50000,10000,10000,20000]}
df=p.DataFrame(d)
av=df.pivot_table(index=['dept','type'],values='salary',aggfunc='mean')
print("average salary from each dept:\n",av)
sm=df.pivot_table(index=['type'],values='salary',aggfunc=['sum','mean','count'])
sm.columns=['total salary','meansalary','numbre of employee']
print("\n sum and mean of:\n",sm)
st=df.pivot_table(values='salary',index='type',aggfunc='std')
print("\n standard deviation:\n",st)

