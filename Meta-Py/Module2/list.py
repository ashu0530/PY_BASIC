list1 = [1,2,3,4,5]

print(list1[2])

print(list1,sep="  ")
print(list1)
print(*list1)

list1.insert(len(list1), 6)
print(list1,sep="  ")
list1.append(7)
print(*list1)
list1.extend([6,7,8,9])
print(list1,sep="  ")

list1.pop(4)
print(list1,sep="  ")


#iterate in list

for x in list1:
    print('value: ', x)


list2 = ['a','b','c']
list3 = ['hello',1,True,40.22]

list4_nested = [1,[2,3,4],5,6]
print(list4_nested[1])




