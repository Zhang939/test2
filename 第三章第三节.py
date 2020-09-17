import operator
print (operator.le((1,2,3),(4,5,6)))
print (operator.le((1,2,3),(1,2,3)))
print (operator.le((1,2,3),(1,5,6)))
print (operator.le((1,2,3),(1,1,6)))
print (operator.le(("a",2,3),("b",5,6)))
print (operator.le((1,2,3),(4,1,6)))