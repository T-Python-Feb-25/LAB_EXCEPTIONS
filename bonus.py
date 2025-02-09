
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
      while True:
        try:
            #طلب ادخال الدرجه و الوحده من اليوزر
            user_input = input('Enter a temperature and its unit(e.g., "25 C" or "77 F"):')
            #فصل الرقم
            temperature_value, unit = user_input.split()
            # تحويل الرقم الى float
            temperature_value = float(temperature_value)

            # تحققلامن الوحده
            if unit.upper() == "C":
                result = celsius_to_fahrenheit(temperature_value)
                print(f"Temperature in Fahrenhit: {result:.2f} F")
            elif unit.upper() == "F":
                result = fahrenheit_to_celsius(temperature_value)
                print(f"Temperature in Celsius: {result:.2f} C")
                #  اذا كانت غير صحيحه استثناء 
            else:
                raise TypeError
            # تم التحويل بنجاح خروج
            break

        except ValueError:
            print("invalid temperature value. Please enter a valid number.")
        except TypeError:
            print('Invalid unit. Please use "C" for celsius or "F" for Fahrenheit.')

main()            

