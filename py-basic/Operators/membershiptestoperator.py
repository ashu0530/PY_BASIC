'''String : check for substring
    Dictionary: check for key
'''

#Strings check 
s = "Ashutosh"
print("A" in s, "B" in s)



#Dictionary check
d = {10:"abc", 20:"efg"}

print(10 in d)
print(id(d))
print(15 in d)
print("abc" in d)


l = [10,20,30,15]
print(30 in l)
print([20,30] in l)


print(30 not in l)
print( 40 not in l)

print([20,30] not in l)



