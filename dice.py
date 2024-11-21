import random
def diceroll():
    print("Please roll the dice.")
    dice = random.randint(1,6)
    print("You got this Number", dice)
while True:
    diceroll()
    option = input("Do you want to play again? (yes/no): ").lower()
    if option != "yes":
            print("Thank you for playing!")
            break