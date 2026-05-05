#~~~~~~~~~~~~~ Simple Calculator in Python ~~~~~~~~~~~~~#
# This is a simple calculator program that allows the user to perform basic arithmetic operations such as addition
# subtraction, multiplication, and division. The user is prompted to enter two numbers and an operator, and the program calculates and displays the result based on the selected operator. The program also handles division by zero and invalid operator inputs gracefully.

# Introduction
print("Hello There.....!")
print(" Iam a simple calculator that can perform basic arithmetic operations.")
print("Enter the two numbers that you want to calculate and the operator you want to use, and I will give you the result. Let's get started!")

# Take input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Calculate based on operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero"
else:
    result = "Invalid operator"

# Shows the result to user
print("Result:", result)
