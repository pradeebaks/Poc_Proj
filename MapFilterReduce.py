l =[1,2,3,4,5,17]
def sq(x): return x*x
print(list(map(sq,l)))
print(list(map((lambda x : x*x),l)))



# t = [x if x>10 else x+10 for x in l]
# print(t)

def square(x):
    return (x ** 2)
def cube(x):
    return (x ** 3)
funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print (tuple(value))

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
def add (a,b,c):
    return a+b+c
print (list(map(add, x, y,z)))  # output [5, 7, 9]


print(list(range(-5,5,2)))
j=filter((lambda x: x<0),range(-5,5))
print(list(j))

a = [1,2,3,7,8,4]
b=[2,4]

r= list( x for x in a if x in b)
print(r)

from functools import reduce as res

g= res((lambda x,y:x+y),[1,2,3,4,5])
print (g)

L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
print(res((lambda x,y: x+y),L))
#both are same
print("".join(L))