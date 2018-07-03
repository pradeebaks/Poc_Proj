#Pandas
#series,dataframe,panel,date_range
import numpy as np

import pandas as pd

# s=pd.Series([1,2,3,4,54])
# print(s)
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#print(ts)

dates = pd.date_range('20130101', periods=6)
print(dates)

# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# print(df.values)
# print(df.dtypes)
# print(df.head(2))
# print(df.tail(2))
# print(df.index)
# print(df.columns)
# print(df)
# print(df.T)



D={'name':['Pradeeba','Sarathy','Vaniksha','Nithya','Shanmugam','TamilSelvi','Sam'], 'Age':[30,34,2,34,62,52,None],   'City':['CHENNAI','CHENNAI',None,'CHENNAI','CHENNAI',None,None]}
Df = pd.DataFrame(D)
# # print(Df)
# #
# # row,col = Df.shape
# # print(row, col)
#
Df["Age"].fillna(0, inplace=True)
Df["City"].fillna("THANJAVUR", inplace=True)
# # print(Df)
# # print (Df["Age"].mean())
# # print (Df.groupby("City"))
# # print(Df.values)
# # print(Df[['name','City']][Df["Age"]<=2])
# Df.set_index("name", inplace=True)
print(Df)
# # print(Df.loc["Pradeeba"])
# #
# # Df.dropna(how="all")
#
g= Df.groupby("City")

for x,y in g:
    print(x)
    print(y)

# print(g.get_group('CHENNAI'))
g.plot()
#Df.plot(kind="bar")

import matplotlib.pyplot as plt
x_pos =list(range(len(D["name"])))
plt.xticks(x_pos, Df["name"])
plt.ylabel('Age')
plt.xlabel("Name")
plt.title('Family Metrics')
plt.show()