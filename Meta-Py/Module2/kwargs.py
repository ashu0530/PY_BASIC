#Args and keywords args

def sum_of(a,b):
    return a+b

print(sum_of(4,5))


def sum_of(a,b):
    return a+b

#print(sum_of(4,5,6))   #Cannot be taken by fun 3 args 
#Args

def sum_of(*args):        
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(4,5,6))   #you can pass any no of argruments


#Kwargs

def sum_of(**kwargs):        
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)
print(sum_of(coffee=2.99, cake=4.55, juice=2.99)) 
