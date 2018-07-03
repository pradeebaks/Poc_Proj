

#Public

class cls:
    var1=10
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        return c

obj = cls(10,20)
print(obj.a)
print(obj.b)
print(obj.var1)
print(obj.add())

#protected

class cls1:
    _x=10
    def __init__(self,a,b):
        self.a=a
        self._b=b
    def add(self):
        c=self.a+self._b
        return c
class cls2(cls1):
    _y=20
    def sub(self):
        return self.a - self._b

obj1 = cls1(10, 20)
print(obj1.a)
print(obj1._b)
print(obj1._x)
print(obj1.add())
obj2 = cls2(20, 10)
print(obj2.a)
print(obj2._y)
print(obj2._b)

#private

class cls3:
    _x=10
    __y=20
    def __init__(self,a,b):
        self.a=a
        self.__b=b
    def add(self):
        c=self.a+self.__b
        return c
class cls4(cls3):
    __y=40
    def sub(self):
        return self.a - self.__b


obj5 = cls3(2,4)
print(obj5.a)
print(obj5._x)
print(obj5.add())

print(obj5._cls3__y) # on the worst case can access the private variable using the classnm
print(obj5._cls3__b)

obj6=cls4(5,3)
print(obj6.a)
print(obj6.sub())

print(obj6.__y)
print(obj6.__b)

#Global

cnt=1

def printf():
    print ("going to print")
    def printff():
        global cnt
        while (cnt<10):
            print("count is  ,",cnt)
            cnt +=1
    return printff
v=printf()
v()

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)




