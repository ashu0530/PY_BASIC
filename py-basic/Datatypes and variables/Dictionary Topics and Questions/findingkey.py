# Python code to demonstrate Dictionary and
# missing value error
d = { 'a' : 1 , 'b' : 2 }

# trying to output value of absent key 
#print ("The value associated with 'c' is : ")
#print (d['c'])


'''Handling Missing Keys in Python Dictionaries
There are the methods to handle missing keys in Python Dictionaries.

Using key
Using get()
Using setdefault()
Using defaultdict()
Using try-except block  '''

ele = {'a': 5, 'c': 8, 'e': 2}
if "a" in ele:
	print(ele["a"])
else:
	print("Key not found")

'''Python Program to Handling Missing keys in Dictionaries Using get()
get(key,def_val) method is useful when we have to check for the key. If the key is present, the value associated with the key is printed, else the def_value passed in arguments is returned.
'''


country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))


'''In Python, the setdefault() method is used with dictionaries to retrieve a value for a specified key. If the key does not exist in the dictionary, setdefault() 
inserts the key with a specified default value and then returns that value. If the key exists, it simply returns the current value of the key.'''

my_dict = {'a': 1, 'b': 2}

# If key exists, it returns the value of the key
print(my_dict.setdefault('a', 10))  # Output: 1

# If key does not exist, it adds the key with the default value and returns the default value
print(my_dict.setdefault('c', 3))  # Output: 3

# Check the updated dictionary
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}


'''Handling Missing keys in Python Dictionaries Using the try-except block
This program shows how to handle missing keys in Python dictionaries using a try-except block. In this example, we are using try-except block to check whether the key is present or not.'''

country_code = {'India': '0091',
				'Australia': '0025',
				'Nepal': '00977'}

try:
	print(country_code['India'])
	print(country_code['USA'])
except KeyError:
	print('Not Found')
