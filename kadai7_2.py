import random

def random_number():
    return random.rondint(100,999)

def input():
    ask = int(input("Enter a 3-digit number: "))
    if 100 <= ask <= 999:
        return ask
    else:
        print("Please enter a 3-digit number.")

def feedback(random_number, ask):
    if ask == random_number:
        print("Correct!")
    else:
        if ask < random_number:
            print("Hint: The correct number is higher.")
        else:
            print("Hint: The correct number is lower.")
            