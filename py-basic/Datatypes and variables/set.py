#Set is data structure where items are distinct elements and unordered , No indexing
#Union, Intersection, Set Difference are fast in sets
#Using hashing internally


s1 = {10,20,30}
print(s1)

s2 = set([20,30,40])   #here set constructor is used to convert any tuple or list into set 
print(s2)

s3 = {}        #empty dictionary
print(type(s3))

s4 = set()  #Constructor 
s5 = set([])

print(type(s4))
print(type(s5))
print(s4)
print(s5)


s = {10,20}
s.add(30)
print(s)

s.add(30)  #Nothing change set have unique value
s.update([40,50]) #added 40 and 50 via list
print(s)

s.update([60,70], [80,90])
print(s)

print()

#Removal operation on set
print("Removal Operation\n")
s ={10,20,30,40}
s.discard(30)
s.discard(50)  #doesn't do anything if value is not present in set 
print(s)

s.remove(20)
print(s)
#s.remove(100)  #Raise an error   #careful usecase like membership

s.clear()
print(s)

s.add(50)
print(s)
del s  #Whole object is delete 
#print(s)



#Boolean operation 
print()
print("In operation\n")

s = {10,20,30,40}
print(len(s))

print ( 20 in s)     #In operation is fast on set compare to list coz set use hashing internally
print(50 in s)


#Two set operations
print()
print("Two set operations\n")

s1 = {2,4,6,8}
s2 = {3,6,9}

print(s1 | s2)  #union operation
print(s1.union(s2))

print(s1 & s2) #and operatior intersection / common element in both set
print(s1.intersection(s2))

print(s1 - s2) #Difference
print(s1.difference(s2))
print(s2.difference(s1))

print(s1 ^ s2)  #bit wise operator for symmetric difference in set both present not common
print(s1.symmetric_difference(s2))


print()
s1 = {2,4,6,8}
s2 = {4,8}

print(s1.isdisjoint(s2)) #Give boolean value if there is no common element give true else false

print(s1.issubset(s2)) #False coz s1 have 4 element and s2 have 2 element
print(s1 <= s2)

print(s1 < s2) #element should not be same

print(s1.issuperset(s2)) #S1 have all the element which present in s2
print(s1>=s2)

print(s1>s2) #proper superset