class NotNumberException(Exception):
    """the value is not a number """
def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32,2)
    
def fahrenheit_to_celsius(fahrenheit):
    return round(((fahrenheit - 32) * 5/9)   ,2)
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    print("--- Welcome to tempreture converter --- ")
    temp = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
    try:
        user_input = temp.split(" ")
        if len(user_input) != 2:
            raise ValueError('please privide a temperature and its unit (e.g., "25 C" or "77 F")')
        if not is_number(user_input[0]):
            raise ValueError("please enter a number")
        if user_input[1] != "C" and user_input[1] != "F":
            raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        if user_input[1] == "F":
            print(f"Temperature in Celsius: {fahrenheit_to_celsius(float(user_input[0]))} C")
        else:
            print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(float(user_input[0]))} F")
    except Exception as e:
        print(e)
        
        
        
while True:
    main()