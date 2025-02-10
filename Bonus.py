def celsius_to_fahrenheit(value):
    fahrenheit = (value * 9/5) + 32
    fahrenheit= round(fahrenheit)
    return fahrenheit
    
def fahrenheit_to_celsius(value):
    celsius = (value - 32) * 5/9
    celsius=round(celsius)
    return celsius
def main():
    while True:
        try:
            user_input = input(f'Enter a temperature and its unit either "C" for Celsius or "F" for Fahrenheit: ').strip()
            value=''.join(filter(str.isdigit, user_input))
            unit=''.join(filter(str.isalpha, user_input))
            value= int(value)
            unit = unit.upper()
            #print(value)
            #print(unit)
            if (unit=="C"):
                print(f"{celsius_to_fahrenheit(value)} F")
                input(" ")
            elif(unit=="F"):
                print(f"{fahrenheit_to_celsius(value)} C")
                input(" ")
            else:
                raise TypeError(" Invalid unit, Enter C  for Celsius  or F for Fahrenheit")  
        except ValueError:
            print("Invalid temperature value. Please enter a temperature number.")
        except TypeError as e:
            print(e, "\n")
            
        except Exception as e:
            print(e)
            

if __name__ == "__main__":
    main()  
  