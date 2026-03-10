num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Choose operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    print("Invalid operator")
    result = None

if result != None:
    print("Result:", result)
