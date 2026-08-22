# i fixed code and this is work now.
# this is a easy code.
num_1 = float(input(" enter first number: "))
num_2 = float(input(" enter first number: "))

operator = input(" select your oprerator ( *, /, +, _): ")

if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)

else:print("That is not valid operator")
