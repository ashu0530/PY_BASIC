'''
There are two file handling functions in Python, open and close. Let's explore the open 
function first. The open function is used for reading, writing and creating files.

The open function accepts two arguments. 
The first is the file name and or the file location and the second argument is the mode. 
The mode indicates what action is required such as reading, writing or creating. 
It's also specifies if you want the file output in text or binary format.

'''

#open(<File name> < file location>, <mode> ) --> Two arguments  #mode = action read,write,creating
#mode = 'r'  in text format read , 'rb' in binary, r+ reading and writing,  w - opens for writing also overwrite

#close()  the open file connection 

#There is one more way to open and close a file in Python and that's with open function. The advantage of using it is that it closes the file automatically.

#Example
#with open ('testing.txt', 'r') as file:

'''
 In Python, you generally handle files in two ways, either in text or binary format. 
 The text format is more user friendly because humans can read. You won't be able to read 
 files in binary formats, but they are much more compact and therefore result in better 
 performance. 

'''

file = open('test.txt', mode = 'r')
data = file.readline()
print(data)
file.close()


#better with exception handling with open , automatically close the file

with open('test.txt', mode = 'r') as file:
    data = file.readline()  
    print(data)



#Creating files 
with open('newfile.txt', mode='w') as file:
    file.write("This is new file created!")

#multiplelines in a file  writelines is accept as list

with open('newfile.txt', mode='w') as file:
    file.writelines(["This is new file created!", "\nAnother line created"])

with open('newfile.txt', mode='a') as file:
    file.writelines(["\nappend line"])


#Exception handling
try:
    with open('sample/newfile.txt', mode='a') as file:
        file.writelines(["\nexceptional handling"])
except FileNotFoundError as e:
    print("ERROR FILE NOT FOUND", e)



#Reading content of a file
'''
Python offers several built-in functions that make this easier. The three methods we'll 
are read, readline, and readlines. 
Let's start with read. The read method returns the entire contents of the file as a string that 
will contain all the characters. You can also pass in an integer to return only the specified
 number of characters in the file. 
 
 The second method to read files in Python is readline

'''
#read()
with open('test.txt', 'r') as file:
    print(file.read())

#readline()
with open('testing.txt', 'r') as file:
    print(file.readline())  #first line
    print(file.readlines())  #First 5 character

#readlines() The readlines method reads the entire contents of the file and then returns it in an ordered list. This allows you to iterate over the list or pick out specific lines based on a condition
with open('testing.txt', 'r') as file:
    lines = file.readline()
    print(len(lines))
    for line in lines:
        print(line)
