'''
Decimal to binary 

18 

18/2 , Q = 9 , R = 0
9/2  , 4  ,  1
4/2  , 2  , 0
2/2  , 1  , 0
1/2 , 0   , 1  

== 10010

Binary to Decimal

10010
Start with last
0X2^0 + 1x2^1 + 0x2^2 + 0x2^3 + 1x2^4   == 18

'''

print(bin(18))   #0b10010  
print(bin(12))

print(int("0b10010",2))   #Binary to decimal
print(int("0b1100",2))


#Bitwise AND:& operator

x = 3  #011      #in case of 0 we got 0
y = 6  #110
#ans   #010   for and case   here 10 is 2
print(x&y)  

#Bitwise OR:| operator

x = 3  #011    #In case of 1 we got 1
y = 6  #110
#ans   #111   for and case   here 111 is 7
print(x|y)  

#Bitwise XOR:^ operator
x = 3  #011    #In case of two input are same we got 0 else 1
y = 6  #110
#ans   #101   for and case   here 101 is 5
print(x^y)  