my_tuple = 1, ' strings', 4.6, True
my_tuple = (1,'strings', 4.6, True)
print(type(my_tuple))

print(my_tuple.count('strings'))

print(my_tuple.index(4.6))


my_tuple[0] = 5
for x in my_tuple:
    print(x)