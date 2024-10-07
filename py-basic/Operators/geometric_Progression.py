'''
A person gets 5000 as salary on 1st jan 2020. The sal doubles every year, find the salary that the person will get on 1st jan 2030

Ans = 512000

Common ratio is 5000,10000,20000,

Formula  = nth term of GP is ar^n-1  where a --> first term and r --> common ratio

'''

a = int(input("Enter a: "))
r = int(input("Enter r: "))
n = int(input("Enter n: "))

res = a*r**(n-1)
print(res)
