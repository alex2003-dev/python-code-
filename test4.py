<<<<<<< HEAD
import random

number = random.randint(1, 100)
attempts = 0

print("your number from 1 to 100 is ready")

while True:
    user_input = input("your number: ")
    
    if not user_input.isdigit():
        continue  
    
    guess = int(user_input)
    attempts += 1
    
    if guess == number:
        print("You guessed right", number, "for", attempts, "attempts!")
        break
    elif guess < number:
        print("number greater.")
    else:
        print("number less.")
=======

>>>>>>> 626c2920b7513ec9c63bc4ec5d0bfb190d363b49
