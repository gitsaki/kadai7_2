import random

def randomnumber():
    return random.rondint(100,999)

def input():
    ask = int(input("Enter a 3-digit number: "))
    if 100 <= ask <= 999:
        return ask
    else:
        print("Please enter a 3-digit number.")
  