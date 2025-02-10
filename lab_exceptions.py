
try:
    def additoin(x, y):
        x = 10
        y = 20
        print("Addition:", x + b )
    additoin(10, 20)
except NameError as w:
    print("pleas enter only two varible, b is not define")
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



