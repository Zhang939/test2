"""
sum=lambda arg1,arg2:arg1+arg2
print("added results:",sum(10,20))
print("added result:",sum(20,20))
"""

def sum(arg1,arg2):
    total=arg1+arg2
    print("inside:",total)
    return total
all=sum(10,20)
print("outside:",all)