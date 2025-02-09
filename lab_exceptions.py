#Find what type of exception is raised.
#Hanlde the exception in try..except
#If operation successful , print "the operation is successful"
#if operation fails, handle the specific exception that is raised , and print a relevant message.
#def additoin(x, y):
    #x = 10
    #y = 20
    #print("Addition:", x + b)
#additoin(10, 20)
try:
    def additoin(x, y):
        x = 10
        y = 20
        print("Addition:", x + b )
    additoin(10, 20)
except NameError as w:
    print("pleas enter only two numbers, b is not define")
except Exception as w:
    print(w.__class__)
#another examele for error
except SyntaxError as w:
    print("pleas check your syntax")
except TypeError as w:
    print("you have a type error pls check your code")
except:
    print("somthing went wrong, check your code")
else:
    print("the operation is successful")





#try:
    #num1:int =int( input("pleas entre any num to multiply it : "))
    #num2:int=int(input("lpeas entre sec num to multiply it : "))
    #reslt:int = num1*num2
   # print(reslt)
#except ValueError:
 #   print("provid num")
#except Exception as e:
   # print(e.__class__)
#print("yeeaaaaiiiiiiii")
