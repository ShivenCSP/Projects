import math

operation = input("What operation would you like to use?(if exponent num1^num2 format)")
num1 = int(input("What is the first number?"))
num2 = int(input("What is the second number?"))

operation = operation.lower()

if operation in ["+", "add", "addition"]:
    print(f"Here is your sum, {num1 + num2}")
elif operation in ["-", "subtract", "difference"]:
    print(f"Here is your difference, {num1 - num2}")
elif operation in ["x", "*", "multiply", "multiplication"]:
    print(f"Here is your product, {num1 * num2}")
elif operation in ["/", "divide", "division"]:
    print(f"Here is your quotient, {num1/num2}")
elif operation in ["^", "exponent", "exponents", "power", "powers"]:
    print(f"Here is your exponent, {num1 ** num2}")
else:
    print("one of your responses are invalid")