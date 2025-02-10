def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
    except NameError as e:
        print(e.__class__ , "Please define a variable before use it the code . ")
    except Exception as e:
        print( f"The type of the exception is :{e.__class__ } for details:  {e}")
    else:
        print("The operation is seccesful ")
        

additoin(10, 20)