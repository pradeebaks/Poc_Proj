x=100
y=12893.973
z="test"
a=['a','b','c']

print("print list {} {} {}".format(a[0],a[1],a[2]))
print ("print number %d " %(x))
print ("print float %.2f " %(y))
print("print variable value :", z)

l =[1,2,3,]
l.append(4,)
print(l)

t2 =(1,2,3,4)+(5,6)
t1 =(2,3)
t =t1+t2
print(t)
#removes duplicate and arranges in order
s ={5,5,6,8,2,5,9}
print(s)
s={'a','c','m','w','a','m','d','k','s','b'}
print(s)

d ={'a':10,'b':20,'c':25}
for i,j in d.items():
    print(i, "=" ,j)
    #print(j)


y =[ x*x if x==2 else x+x for x in l]
print (y)

