import random

levelEasy = 10
levelHard = 5
level = 0

print = ('''



''')
print("Welcome to the Number Guessing Game!")

numberToGuess = random.randint(1, 100)
#print(f"Psst, number to guess is {numberToGuess}")

levelDefine = input("Choose the difficulty. Type 'easy' of 'hard': ")

if levelDefine == "easy":
    level = levelEasy
elif levelDefine == "hard":
    level = levelHard
else:
    raise Exception("Entered commands is out of list of possible commands")

while level != 0:

    print(f"You {level} attempts remaining to guess the number")
    guess = int(input("Make a guess, enter the number between 1 and 100: "))
    level -= 1

    if guess == numberToGuess:
        print(f"You got it, the answer was {guess}")
        exit()    
    elif guess > numberToGuess:
        print(" Too high!")
    elif guess < numberToGuess:    
        print(" Too low!")

print("You've run out of quesses, you lose.")

for in range