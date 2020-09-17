"""
def printme(str):
    print(str)
    return
printme(str)
"""

"""
def printinfo(name,age):
    print("name:",name)
    print("age:",age)
    return
printinfo(age=50,name="Runoob")
"""

"""
def printinfo(name,age=45):
    print("name:",name)
    print("age:",age)
    return
printinfo(age=50,name="Udbs")
print("-------------------")
printinfo(name="Udbs")
"""

def printinfo(agel,*vartuple):
    print("print:")
    print(agel)
    for var in vartuple:
        print(var)
    return
printinfo(10)
printinfo(70,60,50)
