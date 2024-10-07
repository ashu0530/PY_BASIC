a = 10
b = 20
c = 30

print(a<b and b<c)
print(a<b or b>c)
print(not a>b)



s1 =""
s2 = s1 or "DefaultStr"
print(s2)


x = 10         #non zero which is true
print(x or 20)

y = 0       #False zero value
print(y or 30)

z = 40   #First evaulated value is non zero then other value is evaulated
print(z and 50)