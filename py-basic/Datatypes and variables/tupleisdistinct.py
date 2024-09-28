#Given a tuple A , find if all elements of tuple are different or not.

#Example 1:

#Input:
#A = (1, 2, 3, 4, 5, 4)
#Output: 
#Not Distinct
#Example 2:

#Input:
#A = (1, 2, 3, 4, 5)
#Output: 
#Distinct

def checkDistinct(A):
    if len(A) == len(set(A)):
        print("Distinct")
    else:
        print("Not Distinct")



A = (1, 2, 3, 4, 5, 4)
checkDistinct(A)