"""
total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print("inside -- Local variables:",total)
    return total
sum(10,20)
print("outside -- G;obal variables:",total)
"""
Money=2000
def AddMoney():
    global Money
    Money+=1
print(Money)
AddMoney()
print(Money)
