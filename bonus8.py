
print("Welcome in the transfer tempreature app")

def celsius_to_fahrenheit (celsius):
    return (celsius * 9 / 5) + 32
        
def fahrenheit_to_celsius (fahrenheit):    
    return (fahrenheit - 32) * 9 / 5 
    

def main ():
    while True :      
        try:   
            User1 = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ").strip()
            TempValue, unit = User1.split()
            
            TempValue = float(TempValue)
            
            if unit.upper() == "C":
                converted_temp = celsius_to_fahrenheit(TempValue)
                print(f"Temperature in Fahrenheit: {converted_temp:.2f} F")
            elif unit.upper() == "F": 
                converted_temp = fahrenheit_to_celsius(TempValue)
                print(f"Temperature in Celsius: {converted_temp:.2f} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            break
        
        except NameError:
            print("Error: A variable is not defined. please check your code.")
        except ValueError: 
            print("please write correct numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
main()