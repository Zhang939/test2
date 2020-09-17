"""
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'=',x,'*',n//x)
            break
    else:
        print(n,'is prime number')
"""

number=7
guess=-1
print("Guess a number game")
while guess!=number:
    guess=int(input("Enter your guess number:"))
    if guess==number:
        print("Congratulations!")
    if guess<number:
        print("The number is small")
    if guess>number:
        print("The number is big")
