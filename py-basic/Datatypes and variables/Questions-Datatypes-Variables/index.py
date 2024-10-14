'''
A = [1,2,3,4,5]
X = 3
O/P: 2

'''



l = [1, 2, 3, 4, 5]
x = int(input("Enter the number: "))  # Convert input to an integer

if x in l:
    index = l.index(x)  # Find the index of x
    print(f"Number {x} found at index: {index}")
else:
    print(f"{x} not found in the list.")


l = [1, 2, 3, 4, 5]
x = int(input("Enter the number: "))  # Convert input to an integer

found = False
for index, value in enumerate(l):
    if value == x:
        print(f"Number {x} found at index: {index}")
        found = True
        break

if not found:
    print(f"{x} not found in the list.")



