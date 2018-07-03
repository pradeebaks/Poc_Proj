import copy

l1 =[1,2,[3,4],5]

#l2 = copy.deepcopy(l1)
l2 = copy.copy(l1)
print(l1)
print(l2)

#make changes
l2[2][0]=10

print(l1)
print(l2)