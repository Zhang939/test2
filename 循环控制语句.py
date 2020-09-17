"""
for letter in 'Python':
    if letter=='h':
        break
    print("Current letter:",letter)

var=10
while var>0:
    print("Current variable value:",var)
    var-=1
    if var==5:
        break
print("Good bye!")
"""

"""
for letter in 'Python':
    if letter=='h':
        continue
    print("Current letter:",letter)

var=10
while var>0:
    var-=1
    if var==5:
        continue
    print("Current variable value:", var)
print("Good bye!")
"""

for letter in 'Python':
    if letter=='h':
        pass
        print("This is pass block")
    print("Current letter:",letter)
print("Good bye!")