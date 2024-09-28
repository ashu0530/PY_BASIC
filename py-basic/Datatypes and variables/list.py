l = [ 10,20,30,40,50]
print(l)
print(l[3])
print(l[-1])
print(l[-2])



l.append(30)   #append value at last of list
print(l)

l.insert(1,15)   #insert the item at given index remaining item shift right side
print(l)

print(15 in l) #Checking item in list return bool value 
print(16 in l)

print(l.count(30)) #How many occurance in list of the items
print(l.index(30)) #tell the first index of occurance of items

print(l.index(30,4,7)) #check 4 to 6 index


print(20 in l)   #Removed function value in list and return remaining list
l.remove(20)
print(l)

print(l.pop())  #Remove last item in list
print(l)


print(l.pop(2))  #Pop with index 
print(l)


del l[1]  #remove item at index 1
print(l)

del l[0:2] #remove via index range
print(l)


a = [ 10,40,20,50]

print(max(a)) #max in list
print(min(a)) #min in list
print(sum(a))

a.reverse()  #reverse the list
print(a) 

a.sort()  #sort in increasing order
print(a)


 

