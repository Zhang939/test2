"""
s='Hello,Runoob'
print(str(s))
print(repr(s))
print(str(1/7))
x=10*3.25
y=200*200
s='x value:'+str(x)+', y value:'+str(y)+'...'
print(s)
"""

"""
hello='hello,runoob\n'
hellos=repr(hello)
print(hellos)
h="hello,runoob\n"
print(h)


a=(1,2,('Google','Runoob'))
print(a[2][0])
"""

"""
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))

for x in range(1,11):
    print(repr(x).ljust(2),repr(x*x).ljust(3),repr(x*x*x).ljust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))


a,b=2,3
print(a,b)
"""

"""
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('{}URL:"{}!"'.format('udbs','www.udbs.cn'))
"""

"""
print('{0} and {1}'.format('Google','udbs'))
print('{1} and {0}'.format('Google','udbs'))
print('{name}URL:{site}'.format(name='udbs',site='www.udbs.cn'))
print('URL list {0},{1}, and {other}.'.format('Google','udbs',other='Taobao'))
"""

import math
print('Approximate value of PI:{:.3f}.'.format(math.pi))
table={'Google':1,'udbs':2,'Taobao':3}
for name,number in table.items():
    print('{0:10}==>{1:10d}'.format(name,number))

import math
print("PI:%5.3f."%math.pi)
