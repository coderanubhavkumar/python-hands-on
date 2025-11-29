pinCode = "1234"
tries = 3
balance = 1000.0  

def showBalance():
    print("Your Balance:", balance)

print("ATM LOGIN ")
print("Please enter your PIN.")

while tries > 0:
    userPin = input("PIN: ")

    if userPin == pinCode:
        print("Login successful!\n")

        while True:
            print("1. Check Balance")
            print("2. Logout")
            choice = input("Choose: ")

            if choice == "1":
                showBalance()
                print()  
            elif choice == "2":
                print("Logging out.")
                break
            else:
                print("Invalid choice, try again.\n")
        break

    else:
        tries -= 1
        print("Wrong PIN. Attempts left:", tries)

        if tries == 0:
            print("Too many wrong attempts. Card blocked.")
