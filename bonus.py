def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        # Prompt the user for input
        temperature = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
        try:
            temp, unit = temperature.split()
            temp = float(temp)
            if unit.upper() == 'C':
                converted_temp = celsius_to_fahrenheit(temp)
                print(f"Temperature in Fahrenheit: {converted_temp:.2f} F")
            elif unit.upper() == 'F':
                converted_temp = fahrenheit_to_celsius(temp)
                print(f"Temperature in Celsius: {converted_temp:.2f} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature value. Please enter a valid temperature value.")
        except TypeError as te:
            print(te)
main()