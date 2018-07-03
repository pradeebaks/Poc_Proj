class clsname:
    x=10
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def add (self):
        c=self.a+self.b
        return c
    def sub (self,c):
        return (c - self.a)


obj = clsname(2,3)
print(obj.add())
print(obj.sub(10))