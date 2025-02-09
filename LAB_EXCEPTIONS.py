def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
    except NameError as e:
        print(f"Name Error happen :{e}")
    except Exception as e:
        print(e.__class__)
    else:
        print("the operation is successful")
        



additoin(10, 20)