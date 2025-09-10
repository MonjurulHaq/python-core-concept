# Variables in Python - Simple Examples

# 1. Basic variable assignment
name = "Monjurul"
age = 22
height = 5.9
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# 2. Multiple assignment
x, y, z = 1, 2, 3
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")


# 3. Variable reassignment
score = 85
print(f"\nInitial score: {score}")
score = 92  # Reassigning the variable
print(f"Updated score: {score}")

# 4. Type checking
print(f"\nVariable types:")
print(f"name is {type(name)}")
print(f"age is {type(age)}")
print(f"height is {type(height)}")
print(f"is_student is {type(is_student)}")

# Example of input type variable
user_input = input("\nEnter something: ")
print(f"You entered: {user_input}")
print(f"user_input is {type(user_input)}")


# # Taking integer input - Method 2: Direct conversion in input
# score_input = int(input("Enter your score: "))
# print(f"Your score: {score_input}")
# print(f"score_input is {type(score_input)}")

# # Taking integer input - Method 3: With error handling
# try:
#     number_input = int(input("Enter a number: "))
#     print(f"Number entered: {number_input}")
#     print(f"number_input is {type(number_input)}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")

# # Taking multiple integers
# print("\nEnter two numbers:")
# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))
# sum_result = num1 + num2
# print(f"Sum of {num1} and {num2} is: {sum_result}")


