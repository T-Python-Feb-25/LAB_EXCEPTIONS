"""
Below you have a code that raises an exception , using what you learned do the following:
Find what type of exception is raised.
Hanlde the exception in try..except
If operation successful , print "the operation is successful"
if operation fails, handle the specific exception that is raised , and print a relevant message.
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)
Bonus
Temperature Converter
Description: In this exercise, you will practice using Python exceptions by creating a simple temperature converter that accepts user input and converts temperatures between Celsius and Fahrenheit. You will handle various exceptions that might arise during the conversion process.


"""

def additoin(x, y):
  try:
    x = 10
    y = 20
    print("Addition:", x + b)

  except NameError as e:
    print(f"Error: {e}. Variable 'b' is not defined try x or y.")
  else:
    print("the operation is successful")






      

additoin(10, 20)

