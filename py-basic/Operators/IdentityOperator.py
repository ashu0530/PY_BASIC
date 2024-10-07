x = 10
y = x

print(id(x), id(y))
print(x is y)
print(x is not y)


#is is not function is depend on id function

x1 = 10
x2 = 10
y1 = 10.5
y2 = 10.5
print(x1 is x2, y1 is y2)


#List operations of identity

l1 = [10,20,30]
l2 = [10,20,30]

l3 = None
l4 = None

print(id(l1), id(l2), id(l3), id(l4))
print(l1 is l2)   #False