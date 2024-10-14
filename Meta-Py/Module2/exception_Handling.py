def divide_by(a,b):
    return a/b

print(divide_by(40,4))
#print(divide_by(40,0))   #Exception error 0 division error

try:
    ans = divide_by(40,0)
except :
    print("Something went wrong")



try:
    ans = divide_by(40,0)
except :
    print("Something went wrong")


'''
Python allows you to make the except statement more specific. 
If you want to trap the exception itself you could add the base class exception right 
after accept. The base class exception is used for all exceptions that are written within 
Python. You can gain access to the exception information by using the as E after exception. 
The E variable acts as an alias for the exception. I can use E to print out the exception in 
the print statement
'''

try:
    ans = divide_by(40,0)
except Exception as e:
    print("Something went wrong!", e)  #division by zero


#In Python, you can also get access to the actual type or class of exception that's occurred.

try:
    ans = divide_by(40,0)
except Exception as e:
    print("Something went wrong!", e)  #division by zero
    print(e.__class__)


#Let's take this one step further to provide even more specific feedback to the end user. In the except statement

try:
    ans = divide_by(40,0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")



def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)


try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")
      