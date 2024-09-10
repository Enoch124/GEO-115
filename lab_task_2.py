#Ask the user to input a number
number = int(input("Enter a number"))

# Check if the number is even or odd
if number % 2== 0:
    print(number, "is even")
else:
    print(number,"is odd")


def is_even(number):
    return number % 2 == 0

# Test the function with one example
number = 7
print(f" The number{number} is even: {is_even(number)}")
    

# Continuously ask the user for input until a valid number is provided
while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print("You entered a valid number:", number)
        break
    except ValueError:
        print("Invalid input, please enter a number.")