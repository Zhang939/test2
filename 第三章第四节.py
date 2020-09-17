""""
a = {"name":"udbs","age":20,"company":"IT"}
print ("a['age']:",a['age'])
a['age'] = 8
a['school'] = "Hadoop School"
print (a)
del a["name"]
print (a)
a.clear()
print (a)
del aprint (a)
"""
"""
a = {"name":"udbs","age":20,"company":"IT","name":"Oracle"}
print (a)
b = a.copy()
print (b)
"""

b = dict.fromkeys(['name',"age"],["udbs",10])
print (b)
a = {"name":"udbs","age":20,"company":"IT","name":"Oracle"}
print (a.get ("name"))
print (a.items())
print (a.keys())
print (a.values())

