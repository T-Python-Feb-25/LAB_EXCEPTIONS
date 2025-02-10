print("Welcome")
print("-" * 20)

def addition():
    while True:
        try:
            X = int(input("Enter first value: "))
            Y = int(input("Enter second value: "))
            Add = X + Y

            #cheak if the numbers is positive 
            if X < 0 or Y < 0:
                print("Please enter positive numbers!")
                continue  #
            
            print(f"The operation is successful,\nThe answer is: {Add}")
            break  # break if the number is correct
        
        except ValueError: 
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

addition()
