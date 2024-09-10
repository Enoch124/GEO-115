#Nested if-else
mark = int(input("Enter mark"))
if mark <=50:
    print("Student fail")
elif 50 < mark <= 60:
    print("Student got: D")
elif 60 < mark <= 75:
    print("Student got: D+")
elif 75 < mark <= 80:
    print("Student got : B")
elif 85 < mark <= 90:
    print("Student got: B+ ")
elif 90 < mark <= 95:
    print("Student got: A")
else:
    print("Student got: A+")



# Nested If-Else Statements Example: Age Category
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")


# Multiple Conditions Example: Positive, Negative, or Zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

# Boolean Operations Example: Valid Email
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email address")
else:
    print("Invalid email address")

