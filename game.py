import random

print("Welcome to Rock Paper Scissors!")
print("1. rock")
print("2. paper")
print("3. scissors")
print("4. exit")

choices = ["1", "2", "3"]  
while True:
    user = input("\nEnter 1/2/3 (or 4 to exit): ")

    if user == "4":
        print("Goodbye!")
        break

    if user not in ["1", "2", "3"]:
        print("Not a valid choice, try again.")
        continue

    comp = random.choice(choices)
    print("Computer picked:", comp)
    if user == comp:
        print("Tie!")
    elif (user == "1" and comp == "3") or \
         (user == "2" and comp == "1") or \
         (user == "3" and comp == "2"):
        print("You win.")
    else:
        print("You lose.")
