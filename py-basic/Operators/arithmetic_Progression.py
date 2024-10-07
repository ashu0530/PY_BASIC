'''
Arithmetic progression nth term in python

A person gets 5000 salary on 1st august 2020. The salary increases by 2000 every month. Find the salary that persion is going to get on 
1st august 2025

'''

#Ans is 125000
#Nth term = a+(n-1)d   --> a is first term , d is common difference

#I/P: a = 5 , d = 2, n = 5  --> O/P --> 13

a = int(input("Enter a:"))
d = int(input("Enter d:"))
n = int(input("Enter n:"))

res = a+(n-1)*d
print(res)
