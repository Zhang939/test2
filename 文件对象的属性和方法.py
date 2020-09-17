"""
f=open(r"D:\Python文件\练习\new.txt",'w')
f.write("python is a good language.\nyes,it is!\n")
print(f.closed)
f.close()
print(f.closed)
print(f.mode)
print(f.name)
"""

"""
f=open(r"D:\Python文件\练习\new.txt",'r')
str=f.readlines(26)
print(str)
f.close()
"""

"""
f=open(r"D:\Python文件\练习\new.txt",'r')
for line in f:
    print(line,end='$')
f.close()
"""

"""
f=open(r"D:\Python文件\练习\new.txt",'w')
num=f.write("Python is a good language\nYes,it is!\n")
print(num)
f.close()

f=open(r"D:\Python文件\练习\new1.txt",'w')
value=("www.udbs.com",14)
s=str(value)
f.write(s)
f.close()
"""

f=open(r"D:\Python文件\练习\new1.txt",'rb+')
f.write(b'32112fsndiuda')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))
print(f.read(1))
f.close()