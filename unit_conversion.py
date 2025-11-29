def kg_to_lb(k):
    return k * 2.20462

def lb_to_kg(p):
    return p / 2.20462

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9


print("Unit Converter")

while True:

    print("\n1) kg -> pounds")
    print("2) pounds -> kg")
    print("3) C -> F")
    print("4) F -> C")
    print("5) exit")

    ch = input("Pick option: ")

    if ch == "5":
        print("bye!")
        break

    if ch not in ["1","2","3","4"]:
        print("Invalid choice.")
        continue

    val = float(input("Value: "))

    if ch == "1":
        print(val, "kg =", kg_to_lb(val), "pounds")
    elif ch == "2":
        print(val, "pounds =", lb_to_kg(val), "kg")
    elif ch == "3":
        print(val, "C =", c_to_f(val), "F")
    else:
        print(val, "F =", f_to_c(val), "C")
