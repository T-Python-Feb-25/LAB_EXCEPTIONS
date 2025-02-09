

def additoin(x, y):
   try:
     x = 10
     y = 20
     print("Addition:", x + b) #b غير معرف 
     print("the operation is successful")
   except NameError:
      print("An error occurred. Variable b is undefined")


additoin(10, 20)