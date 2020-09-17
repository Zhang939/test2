"""
var1 = 100
if var1:
    print("True")
    print(var1)
var2 =  0
if var2:
    print("True")
    print(var2)
print("Good bye!")
"""

"""
age=int(input("Please enter your dog's age:"))
if age<0:
    print("Just kidding")
elif age==1:
    print("It's 14 years old")
elif age==2:
    print("It's 22 years old")
elif age>2:
    human=22+(age-2)*5
    print("The age:",human)
"""

var=int(input("Please enter a number:"))
if(var%2==0):
    if(var%3==0):
        print("var既能被2整除也能被3整除")
    else:
        print("var能被2整除不能被3整除")
else:
    if(var%3==0):
        print("var不能被2整除但能被3整除")
    else:
        print("var既不能被2整除也不能被3整除")