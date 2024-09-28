#Given a tuple A with distinct elements and an integer X, find the index position of X. Assume to have X in the tuple always.

#Example 1:

#Input:
#A = (1, 2, 3, 4, 5)
#X = 3
#Output: 
#2

#A = (1, 2, 3, 4, 5)
#X = 3
A = (3, 2, 1, 5, 4)
X = 5
for i in range(0,len(A),1):
    if A[i] == X:
        print(i)
