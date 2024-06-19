import random

def random_number():
    return random.randint(100,999)

def user_input():
    while True:
        ask = int(input("Enter a 3-digit number: "))
        if 100 <= ask <= 999:
            return ask
        else:
            print("Please enter a 3-digit number.")

def feedback(correct_number, ask):
    if ask == correct_number:
        print("Correct!")
    else:
        if ask < correct_number:
            print("Hint: The correct number is higher.")
        else:
            print("Hint: The correct number is lower.")

def game():
    max_attempts = 10
    attempts = 0
    correct_number = random_number()

    while attempts < max_attempts:
        guess = user_input()
        attempts += 1
        feedback(correct_number, guess)
        print(f"Attempts: {max_attempts-attempts}")
        if attempts == max_attempts and guess != correct_number:
            print("Game over!")
            break

if __name__ == "__main__":
    game()