"""
Temperature Converter
Description: In this exercise, you will practice using Python exceptions by creating a simple temperature converter that accepts user input and converts temperatures between Celsius and Fahrenheit. You will handle various exceptions that might arise during the conversion process.

Instructions:
Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula fahrenheit = (celsius * 9/5) + 32.

Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula celsius = (fahrenheit - 32) * 5/9.

Write a main function that:

a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F").
b. Splits the input string into a temperature value and its unit.
c. Tries to convert the input temperature to its opposite unit using the appropriate function (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
d. Riases & handles the following exceptions:
ValueError: If the user enters an invalid temperature value, display an error message and prompt the user to try again.
TypeError: raise this error If the user enters an invalid unit, display an error message and prompt the user to try again.
e. If the conversion is successful, print the converted temperature and its unit.
Call the main function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.

Example Output:

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100 F
Temperature in Celsius: 37.78 C

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 50 C
Temperature in Fahrenheit: 122.0 F

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 25 X
Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100.5 F
Temperature in Celsius: 38.06 C

"""

def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

def main():
  count = 5
  while count > 0:
    try:
      user_input = input(f'[{6 - count}/5]Enter a temperature and its unit (e.g., "25 C" or "77 F"):')
      new_temp = user_input.split()
      
      if len(new_temp) != 2:
        raise ValueError("Invalid input. Please enter  temperature and its unit")

      temp_value , unit = new_temp
      temp_value = float(temp_value)
      unit = unit.upper()

      if unit == 'C':
        convert_temp = celsius_to_fahrenheit(temp_value)
        print(f"Temperature in fahrenheit:{convert_temp:.2f}")

      elif unit == 'F':
        convert_temp = fahrenheit_to_celsius(temp_value)
        print(f"Temperature in celsius: {convert_temp:.2f}")

      
      else:
        raise TypeError(f"Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")



    except ValueError as va:
      print(f"Error: {va}. Try again.")

    except TypeError as ty:
      print(f"Error: {ty} . Try again.")

    except Exception as e:
      print(f"An error occurred: {e}. Try again")

    count -= 1

    if count == 0:
          print("Too many failed try . Exiting program.")



main()