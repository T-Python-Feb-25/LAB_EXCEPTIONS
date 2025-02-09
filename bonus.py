def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"Temperature in Fahrenheit: {celsius} F"

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return f"Temperature in Celsius: {celsius} C"


def main():
    while True:
        try:
            userTemperatureAndUnit = input(f'Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
            parts = userTemperatureAndUnit.split()
            value, unit = parts

            value = float(value)
            if unit == "C":
                result = celsius_to_fahrenheit(float(value))
            elif unit == "F":
                result = fahrenheit_to_celsius(float(value))
            else:
                raise TypeError("") 
            
            
                
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid Value. Please use numbers followed by char")
        else:
            print(result)
            break


main()
     