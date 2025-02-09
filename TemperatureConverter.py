def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    print("\t*****Converting Temperatures*****")
    while True:
        try:
            temp=input('Enter a temperature and its unit (e.g., "25 C" or "77 F"):')
            tempList = temp.split(" ")
            value =int(tempList[0])
            unit = tempList[1].upper()
            if unit == 'C':
               print( f"Temperature in Fahrenheit: {round(celsius_to_fahrenheit(value), 2)} F")
               break
            elif unit == 'F':
                print(f"Temperature in celsius: {round(fahrenheit_to_celsius(value), 2)} C")
                break

            if not unit in ['C','F']:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")


        except ValueError:
            print("Invalid value. Please enter a valid number")
            continue
        except TypeError as e:
            print(e)
            continue

if __name__=="__main__":
    main()