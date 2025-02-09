def celsius_to_fahrenheit(celsius):
    try:
     fahrenheit = (celsius * 9/5) + 32
     return fahrenheit 
    except TypeError as e:
        raise TypeError("invalid input: celsius value must number")



def fahernheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit-32)*5/9
        return fahrenheit
    except TypeError as e:
        raise TypeError ("invalid input: fahrenheit value must number")    



def main ():
    while True:

    try:
       user_input=input ("please enter temperature")




       parts = user_input 
       if len(parts) !=2:
            raise ValueError("invalid format.please use the format 'value unit")



value,unit = parts
value= float(value)
unit= unit.upper()


if unit == "C":
    converted = 
