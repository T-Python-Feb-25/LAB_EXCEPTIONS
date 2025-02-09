"""def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)"""





def additoin (x: int, y: int):
    try:
        result = x + y
        print("the operation is successful ")
    except TypeError as e :
        print("error ,we do not accept string inputs ")    


additoin(10,20)        
additoin("one",23)