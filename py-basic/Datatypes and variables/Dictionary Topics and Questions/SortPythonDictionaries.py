#Example 1: Sorting Dictionary By Key
#In this example, we will sort the dictionary by keys and the result type will be a dictionary. 
#Display both the keys and values, sorted by key in alphabetical order.


myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}  #Dictionary created

myKeys = list(myDict.keys())        
print("The keys is:", myKeys)   #save the keys by alphabetical order

myKeys.sort()
print("Keys is in sorted order:", myKeys)   

#sorted_dict = {i: myDict[i] for i in myKeys}
    #print(sorted_dict)

for i in myKeys:
    sorted_dict = {i:myDict[i]}

    print(sorted_dict)
