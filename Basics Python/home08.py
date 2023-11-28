# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operator from the user
operator = input("Enter a mathematical operator (+, -, *, /): ")

# Perform the operation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operator. Please enter +, -, *, or /.")

# Print the result if it's available
if 'result' in locals():
    print(f"Your Answer is: {result}")
