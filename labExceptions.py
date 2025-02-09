try:

    def additoin(x, y):
      x = 10
      y = 20
    print("Addition:", x + b)

except NameError as e :
    print("Make sure that you define your variables before running the program")
    print(e.__class__)


additoin(10, 20)
