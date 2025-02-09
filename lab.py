def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
        
    except NameError as ex:
        print(f"the variable not define is {ex}")
    except Exception as ex:
        print(f"the exception name is {ex.__class__}")
    else:
        print("the operation is successful")

additoin(10, 20)