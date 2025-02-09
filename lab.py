def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

#Task 1: Find what type of exception is raised
try:
    additoin(10, 20)
    print("The operation is successful") #Task 3: If operation successful , print "the operation is successful"
except NameError as ne: #Task 2: Handle the exception in try..except
    print(f"A NameError occurred: {ne}. Try again") #Task 4: if operation fails, handle the specific exception that is raised , and print a relevant message.
