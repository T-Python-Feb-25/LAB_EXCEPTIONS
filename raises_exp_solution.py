def additoin(x, y):
    try:
       x = 10
       y = 20
       if 'b'not in locals() and globals():
        raise NameError("'b' not defind")
       
       print("Addition:", x + b)
       print("the operation is succfull")
    except NameError as e:
     print("the operation is failed",e)
additoin(10,20)
   



    