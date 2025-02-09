def celsius_to_fahrenheit(celsius):
    '''this function convert temperature from celsius_to_fahrenheit 
       args:
            celisus(float):The temperature in Celsius to be converted'''
        
    fahrenheit = round((celsius * 9/5) + 32,2)
    return f"Temperature in Fahrenheit: {fahrenheit} F"
def fahrenheit_to_celsius(fahrenheit):
    '''this function convert temperature from fahrenheit to celsius
       args: 
            fahrenheit(float):The temperature in Fahrenheit to be converted
            '''
    celsius = round((fahrenheit - 32) * 5/9,2)
    return f"Temperature in Celsius: {celsius} C"
while True: 
    try:
        user_input=input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
        user_input=user_input.split(" ")
        temp_value=float(user_input[0])
        temp_unit=user_input[1]
        
        if temp_unit.lower()=="c":
            print(celsius_to_fahrenheit(float(temp_value)))
        elif temp_unit.lower()=="f":
            print(fahrenheit_to_celsius(float(temp_value)))
        else:
            raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Invalid number:{e} ")
    except TypeError as e:
        print(e)
    except Exception as e :
        print(e.__class__)
    else:
        break

    

