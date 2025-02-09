'''
Below you have a code that raises an exception , using what you learned do the following:
- Find what type of exception is raised.
- Hanlde the exception in try..except 
- If operation successful , print "the operation is successful"
- if operation fails, handle the specific exception that is raised , and print a relevant message.
```
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)
'''
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + y)

#Task 1: Find what type of exception is raised
try:
    additoin(10, 20)
    print("The operation is successful")
except NameError as ne: #Task 2: Handle the exception in try..except
    print("A NameError occurred: ", ne)
    
