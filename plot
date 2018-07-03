import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

D={'name':['Pradeeba','Sarathy','Vaniksha','Nithya','Shanmugam','TamilSelvi','Sam'], 'Age':[30,34,2,34,62,52,None]}
df2 = pd.DataFrame(D)
df2.fillna(4, inplace=True)

df2.plot.bar()
x_pos =list(range(len(D["name"])))
plt.xticks(x_pos,df2["name"])
plt.ylabel('Age')
plt.xlabel("Name")
plt.title('Family Metrics')
plt.show()

# df =pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000', periods =10),columns=list('ABCD'))
# df.plot()
# plt.show()