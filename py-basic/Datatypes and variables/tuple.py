t = (10,20,"geeks")
print(t)

t = ()
print(type(t))
print(t)

t = (10) 
print(type(t))  #integer coz single value

t = (10,)
print(type(t))

t = 10,20,30,40,50  #Bracket is optional in python

print(t[2])
print(type(t))
print(t[-1])
print(t[1:3])

print(len(t))
print(t.count(10))
print(t.index(20))