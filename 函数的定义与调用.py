"""
def hello(str):
    print("Hello",str)
    return
string1='World'
hello(string1)
string1=input("Enter a string:")
hello(string1)
"""

"""
def printme(str):
    print(str)
    return
printme("Call printme function")
printme("Call [rintme function again")
"""

def changeme(mylist):
    mylist.append([1,2,3,4])
    print("inside",mylist)
    return
mylist=[10,20,30]
changeme(mylist)
print("outside:",mylist)