#Given two sets A and B. check whether A is subset of B ?

#A is subset of B, if all elements of a set A are present in another set B.

#Example 1:

#Input:
#A = {1, 4, 3}
#B = {1, 4, 3, 2}
#Output: 
#True

A = {1, 4, 3}
B = {1, 4, 3, 2}

print(A.issubset(B))