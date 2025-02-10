def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    while True:
        user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
        try:
            value, unit = user_input.split()

            if not value.isdigit():
                raise ValueError("Invalid temperature value. Please enter a numeric value.")
            
            value = float(value) 

            if unit.upper() not in ['C', 'F']:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

            if unit.upper() == 'C':
                converted = celsius_to_fahrenheit(value)
                print(f"Temperature in Fahrenheit: {converted:.2f} F")
            elif unit.upper() == 'F':
                converted = fahrenheit_to_celsius(value)
                print(f"Temperature in Celsius: {converted:.2f} C")

        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print("An unexpected error occurred:", e)
        else:
            print("the operation is successful")

if __name__ == "__main__":
    main()
             