sample_dict = {1: 'coffee', 2: 'Tea', 3: 'juice'}
print(sample_dict[1])


sample_dict = {1: 'coffee', 2: 'Tea', 3: 'juice'}
sample_dict[2] ='Mint Tea'
print(sample_dict)

sample_dict = {1: 'coffee', 2: 'Tea', 3: 'juice'}
del sample_dict[3]
print(sample_dict)


my_d ={}
print(type(my_d))

my_d ={1:"Test", 'Name':"Ashu"}
print(my_d[1])
my_d[2] = 'Test2'  #key is added
print(my_d )

my_d[1] = "Not a test"
print(my_d)


#iterate
for x in my_d:
    print(x)  #Print keys

#Key + Value

for key, value in my_d.items():
    print(str(key)+ " : " + value)

