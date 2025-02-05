import pandas as pd
import numpy  as np
import matplotlib.pyplot as pl
a={'sumit':[67,45,55,76,82],'rajeev':[85,80,76,78,87],'priya':[88,73,78,92,95],'divya':[72,65,74,83,81]}
b={'col1':[50,None,95.5,82,],'col2':[98.0,65.0,75.0,85.0],'col3':[60.0,57.5,69.5,49.0]}
s1=pd.Series((12,3,45,22,np.NaN),index=('a','b','c','d','e'))
s2=np.arange(1,5)
s3=pd.Series(s2**2,index=s2)
s4=np.array([1,2,3,4,5])
s1.index.name='hi'
s1.name='hello'
s1[0:1]=12
s5=s1.reindex(['c','v','b','n','m'])
print(s5)
c={'name':['nancy drew','hardy boys','diary of a wimpy kid','harry potter'],'price':[150,180,225,500]}
s6=pd.DataFrame(c)
print(s6)
s6['special_price']=[150,180,225,500]
s6.loc['4']=['the secret',800,np.NaN]
del s6['special_price']
for (row,rowseries) in s6.iterrows():
    print('rowindex:',row)
    print('containing:')
    print(rowseries)
x=np.arange(0,10,2)
y=np.arange(0,100,20)
a=np.sin(x)
b=np.cos(x)
pl.plot(x,a,'c+',linestyle='-',linewidth=2,markeredgecolor='b')
pl.plot(x,b,'r',linestyle='-.',linewidth=3)
pl.xlabel('hi')
pl.ylabel('hello')
pl.title('gay')
pl.show()
pl.bar(x,y)
pl.show()