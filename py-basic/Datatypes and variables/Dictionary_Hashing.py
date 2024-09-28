#Dictionary is a collection of key-value pairs, and it is unordered
#All keys must be distinct
#Values can be repeated
#Uses hashing internally
#Hashmap in java
#Real world use case emp id save, student data roll number,Storing frequency of items like voting

print("Dictionary Example")
d = {110:"xyz", 101:"abc", 105:"bcd", 104:"abc"}
print(d)
print(type(d))
print()

print("Operations in Dictionary\n")
d = {110:"abc",101:"xyz",105:"pqr"}
print(d)

d={} #Empty dictionary
print(d)
print(type(d))

d["laptop"] = 40000  #added items in dict or hashmap "Laptop is key"
d["mobile"] = 15000
d["earphone"] = 4000
print(d)
print(d["earphone"])   #4000  #access the key
print()

#Get function in dictionary
print("More operation of dictionary like get\n")
d = {110:"abc",101:"xyz",105:"pqr"}

print(d.get(101)) #Get function key to the get function 
print(d.get(125))  #not present in dictionary it give None, helpful if key doesn't exist in application then it will raise an error like above method.
print(d.get(125,"Na"))  #Print NA 


if 110 in d:
    print(d[110])
else:
    print("NA")
print()


#Get function in dictionary
print("More operation of dictionary like pop,del\n")
d = {110:"abc",101:"xyz",105:"pqr",106:"bcd"}

d[101] ="wxy" #It changes the value corresponding to that keyt
print(len(d)) #How many key-value pairs
print(d)


print(d.pop(105))   #Remove the key-value pair corresponding to the given key and display value of deleted key value
print(d)
 
del d[106]     #it simply delete the value not display the deleted value
print(d)

d[108]="cde"
print(d)
print(d.popitem()) #Remove the last key value pair and return the key-value pair as output
print(d)