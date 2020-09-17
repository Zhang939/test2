"""
class MyClass:
    i=12345
    def f(self):
        return 'Hello world'
x=MyClass()
print("The properties of the MyClass i:",x.i)
print("The method of the MyClass f:",x.f())
"""

"""
class complex:
    def _init_(self,realpart,imagpart):
        self.r=realpartr
        self.i=imagpart
x=complex(3.0,-4.5)
print(x.r,x.i)
"""
class people:
    name=''
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s say:I'm %d."%(self.name,self.age))
p=people('udbs',10,30)
p.speak()

