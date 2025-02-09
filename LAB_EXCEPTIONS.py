def addition():
    try:
        x = int(input("Provide the first number: "))
        y = int(input("Provide the first number"))
        print("Addition:", x + b)

    except NameError:
        print("the Variable is not defined")

    except ValueError:
        print("You have provided an invaled value !!")

    except Exception as e:
        print(e.__class__)
        print("Something went Wrong !!")

    else:
        print("the operation is successful")

    finally:
        print("Thank you for using the additions App")


addition()

'''
this is the first Python lab in the Course
Feb9, 2025
By Mohammed Albushaier
'''
