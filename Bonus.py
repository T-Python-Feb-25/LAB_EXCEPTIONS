#Converts the input in celsius to fahrenheit
def celsius_to_fahrenheit(celsius)->float:
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

#Converts the input in fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit)->float:
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

#this function will ask the user to input and check which function to call or if an error has resin 
def main():

    tempreture= input("Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\"):")
    convertureSign= tempreture.split(" ")
    try:
        if convertureSign[1]=='C':
            fahrenheit=celsius_to_fahrenheit(float (convertureSign[0]))
            print(f"Temperature in Fahrenheit: {fahrenheit} F 2.f")
        elif convertureSign[1]=='F':
            celsius=fahrenheit_to_celsius(float(convertureSign[0]))
            print(f"Temperature in Celsius: {celsius} C  .2 f")
        else:
            print ("Invaled Entry !!")
            main()
    # to handel if the user entered a wrong type of data
    except TypeError as e:
        print (e.__class__)
        print ("unsupported operand")
        main()

    # to handel if the user a value error
    except ValueError as e:
        print (e.__class__)
        print ("You have provided an invaled value !!")
        main()
    # to handel if the user entered
    except IndexError as e:
        print(e.__class__)
        print("you have an Index Error   !!")
        main()
# to handel ALL OTHER EXCEPTIONS
    except Exception as e:
        print(e.__class__)
        print("Something went Wrong  !!")
        main()


''' finally:
        main()'''
# to keep the program running untle the user enters e to exit the program
while True:
    main()
    choice=input ("Would you like to exit the program? enter \"e\" or Any button to continue")
    if choice =='e' or choice=='E':
        break




'''
this is the first Python lab in the Course
Feb9, 2025
By Mohammed Albushaier
'''