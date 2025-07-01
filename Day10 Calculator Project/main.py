from art import logo


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(logo)
if_continue = "y"
result = None
while True:

    if result is None:
        f_num = int(input("Enter your first number: "))
    else:
        f_num = result
    operator = input("Enter your operator: \n+\n-\n*\n/\n")
    s_num = int(input("Enter your second number: "))
    result = operations[operator](f_num, s_num)
    print(result)
    if_continue = input("Do you want to continue? (y/n): ")
    if if_continue == "n":
        print("\n" * 20)
        print(logo)
        result = None