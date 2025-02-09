def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            input_temperature = input("enter the temperature (e.g 25 c , 77 f) : ")
            temp, unit = input_temperature.split()
            temperature_value = float(temp)
            unit = unit.upper()

            if unit == "C":
                convert_temperature = celsius_to_fahrenheit(temperature_value)
                print(f"the temperature {temperature_value} C is {convert_temperature:.2f}F ")
            elif unit == "F":
                convert_temperature = fahrenheit_to_celsius(temperature_value)
                print(f"the temperature {temperature_value} F is {convert_temperature:.2f}C ")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            
        except ValueError as ex:
            print("Invalid temperature value. Please enter a valid number.")
        except TypeError as ex:
            print(ex)

main()



