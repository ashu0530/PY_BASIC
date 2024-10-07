x = 9
y = 4
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)  #Remainder
print(x**y)  #Power operator


x = -5
y = 2
print(x//2)
x = 5.0
y = 2
print(x//2)

x = 2
y = -2
print(x**y)   #2power-2 = 1/4


#Precedence operator
print(5+2*3)
print(5+3*4**2)   #16*3+5

#Associativity                                + - left to right,  * / // left to right ,  ** Right to left, Bracket first evaulated
print(5+4-2)
print(2**2**-1)
print((2**2)**-1)