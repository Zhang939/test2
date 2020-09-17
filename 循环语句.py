"""
n=100
sum=0
counter=1
while counter<=n:
    sum+=counter
    counter+=1
print("sum 1 to %d is %d",n,sum)

count=0
while count<5:
    print(count,'<5')
    count+=1
else:
    print(count,'>=5')
"""

"""
languages=['C','C++','Perl','Python']
for x in languages:
    print(x)
"""

"""
sites=["Baidu","Google","Udbs","Taobao"]
for site in sites:
    if site in "Udbs":
        print("Udbs course")
        print("complete cycle")
        break
    print("Cycle data"+site)
else:
    print("No cycle data")
"""

fruits=['banana','apple','mango']
for index in range(len(fruits)):
    print(index,":",fruits[index])
