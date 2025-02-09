
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    user_input = input("Enter a temperature followed by its unit (e.g., '30 C' or '86 F'): ").split()
    if len(user_input) != 2:
        print("Invalid input format")
        return
    try:
        temp = float(user_input[0])
        unit = user_input[1].upper()
        if unit == "C":
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp}C is {converted:.2f} F")
        elif unit == "F":
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp}F is {converted:.2f} C")
        else:
            print("Unknown unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
main()