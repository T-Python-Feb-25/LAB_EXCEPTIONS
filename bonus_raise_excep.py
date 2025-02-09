def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    """Main function to get user input and perform temperature conversion."""
    while True:
        try:
            # Get user input
            user_enter = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')

            # Split the input into value and unit
            parts = user_enter.split()

            if len(parts) != 2:
                raise ValueError("Invalid input format. Please enter a number followed by 'C' or 'F'.")

            temp_value, unit = parts
            temp_value = float(temp_value)  # Convert to float

            # Perform conversion based on unit
            if unit.upper() == "C":
                converted = celsius_to_fahrenheit(temp_value)
                print(f"Temperature in Fahrenheit: {converted:.2f} F")
            elif unit.upper() == "F":
                converted = fahrenheit_to_celsius(temp_value)
                print(f"Temperature in Celsius: {converted:.2f} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

            break  # Exit the loop if conversion is successful

        except ValueError:
            print("Invalid temperature value. Please enter a valid number.")
        except TypeError as e:
            print(e)

# Run the program
main()