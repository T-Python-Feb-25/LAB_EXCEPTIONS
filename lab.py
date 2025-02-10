def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError:
    print("The error is 'b' not defined ")
except Exception as e:
    print(e)
else:
    print("The operation is successful")