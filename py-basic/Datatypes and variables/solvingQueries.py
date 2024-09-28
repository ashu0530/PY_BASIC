#Given a dictionary, and a list of queries(keys), you have to find and print the value of each query from the dictionary if present else it prints "None".

#Example 1:

#Input:
#dict = {1:"abc", 2: "cde", 3: "fgh"}
#query = [2, 3, 4]
#Output:
#cde
#fgh
#None

dict = {1:"abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]

#for i in query:
#    print(dict[i])

for i in query:
    print(dict.get(i,"None"))
