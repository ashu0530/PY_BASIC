#Given two sets A and B. find the Union of both the sets.

#Union of two given sets A and B is a set which consists of all the elements of A and all the elements of B such that no element is repeated.

#Example 1:

#Input:
#A = {2, 5, 6}
#B = {1, 4, 3, 2}
#Output: 
#1 2 3 4 5 6

A = {2, 5, 6}
B = {1, 4, 3, 2}

ans = A.union(B)
print(ans)