#ClassMethodDecorator
#StaticMethodDecorator
class NumberCls:
    x=10

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add (self):
        return self.a+self.b

    @classmethod
    def multiply(cls,mpl):
        return cls.x*mpl

    @staticmethod
    def sub(c,d):
        return c-d


obj =NumberCls(4,2)
print(obj.add())
print(obj.multiply(2))
print(obj.sub(4,2))


#PropertyDecorator

class employee:
    def __init__(self, fname,lname,empid):
        self.fname  = fname
        self.lname=lname
        self.empid =empid
        self.email= None


    @property
    def fname1 (self):
        return self.fname

    @fname1.setter
    def fname1(self, nw_fname):
        self.fname = nw_fname

    @property
    def emailid(self):
        #return self.fname+self.lname+".gamil.com"
        return self.email


    @emailid.setter
    def emailid (self, newid):
        self.email = newid



emp =employee("Pradeeba","Parthasarathy","29447")
print(emp.fname)
print(emp.fname1)
emp.fname1="vaniksha"
print(emp.fname)
print(emp.fname1)
print(emp.emailid)
emp.emailid ="test@hps.com"
print(emp.emailid)
print(emp.email)

print(emp.fullname)
emp.fullname ="vaniksha parthasarathy"
print(emp.fullname)

#userdefinedDecorator
#Multiple/Nested Decorator

def innerfun1(originalfn):
    print(" Before innerfun1 ", originalfn.__name__)
    def innerfun2(*arg,**kwarg):
        print( " Before innerfun2 " , originalfn.__name__)
        res = originalfn(*arg,**kwarg)
        print(" After innerfun2 ",  originalfn.__name__)
        return res

    print( " After innerfun1 ", originalfn.__name__)
    return innerfun2

def innerfun3(originalfn):
    print( " Before innerfun3 ", originalfn.__name__)
    def innerfun4(*arg,**kwarg):
        print( " Before innerfun4 " , originalfn.__name__)
        res = originalfn(*arg,**kwarg)
        print( " After innerfun4 ",  originalfn.__name__)
        return res
    print( " After innerfun3 ", originalfn.__name__)
    return innerfun4


@innerfun3
@innerfun1
def display(name,age):
    print("name is ", name, " and age is  ", age)

display("Vaniksha",2)

#ParameterizedDecorator


def outerfun(perfix):
    print (perfix, " Before outerfun ")
    def innerfun1(originalfn):
        print(perfix, " Before innerfun1 ", originalfn.__name__)
        def innerfun2(*arg,**kwarg):
            print(perfix, " Before innerfun2 " , originalfn.__name__)
            res = originalfn(*arg,**kwarg)
            print(perfix, " After innerfun2 ",  originalfn.__name__)
            return res

        print(perfix, " After innerfun1 ", originalfn.__name__)
        return innerfun2
    print(perfix, " After outerfun ")
    return innerfun1


@outerfun("Test:")
def display(name,age):
    print("name is ", name, " and age is  ", age)


display("Vaniksha",2)