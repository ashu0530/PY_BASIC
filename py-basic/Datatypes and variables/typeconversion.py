#Type conversion in python 
# Implict and Explict type conversion

a = 10
b = 1.5
c = a+b
print(c)

d = False   #here False is 0 and True is 1 
e = a+d
print(e)



#Explict Type conversion
s = "135"
i = 10+int(s)    #Constructor in integer
print(i)
t = "abc"
#j = 10+int(t)
#print(j)


#Explict convert string to list, tuple, set
s = "Ashutosh"
print(list(s))
print(tuple(s))
print(set(s))

#Explict convert list into string
l = ['a','b','c']
print(str(l))
a = 10
b = 11
print(str(a)+str(b)) #Concanating both string
c = 12.5
print(str(c))

#conversion tuple,set to list
t = (10,20,30) 
print(list(t))

s = {10,20,30}
print(list(s))


#Convert integer to binary,hexa,octal
a = 20
print(bin(a))    #10100
print(hex(a))   #group 4 bits of binary 
print(oct(a)) #Group 3 bits of binary



#Convert String in binary and oct , hex
a = "1001"
print(int(a,2))  #Here 2 is base

b = "12"
print(int(b,8))

c = "A1"   #Here A is treated 10
print(int(c,16))



##Questions   Type cast and double it Given an input num as a string. You need to typecast into an integer and double it.

##Example 1:

##Input:
##num = 5
##Output: 
##10
##Explanation: Just typecast and double it.

num = str(5)
print(type(num))

print(num)
print(int(num)+5)
