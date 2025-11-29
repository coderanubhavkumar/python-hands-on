def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "cant divide by zero"
    return a / b


print("Simple Calculator")

while True:

    print("\n1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Quit\n")

    op = input("Choose option: ")

    if op == "5":
        print("Calculator closed.")
        break

    if op not in ["1", "2", "3", "4"]:
        print("Invalid choice, try again.")
        continue

    
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))

    if op == "1":
        result = add(n1, n2)
    elif op == "2":
        result = sub(n1, n2)
    elif op == "3":
        result = mul(n1, n2)
    else:
        result = div(n1, n2)

    print("Result =", result)
