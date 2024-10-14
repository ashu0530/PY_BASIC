set_a = {1,2,3,4,5,5}
print(set_a) #No duplicate

set_a.add(6) 
print(set_a) #add

set_a.remove(2)
print(set_a) #remove

set_a.discard(3)
print(set_a)


#maths 
set_a = {1,2,3,4,5,5}
set_b = {4,5,6,7,8}

print(set_a.union(set_b))
print(set_a | set_b)

print(set_a.intersection(set_b))
print(set_a & set_b)


print(set_a.difference(set_b))
print(set_a - set_b)


print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)


