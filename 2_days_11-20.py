# DAY 11

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.



# print("Do you want to play a game Blackjack? Type 'y' or 'n' ")

# print("Type 'y' to get another card, type 'n' to pass: ")
# from copy import deepcopy

'''

import random
import os

# from pyrsistent import CheckedKeyTypeError



def dealCard():
    listOfCards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    anotherCard = random.choice(listOfCards)
    return anotherCard

def calculateScore(cardsList): 
    if sum(cardsList) == 21 and len(cardsList) == 2:
        return 0
    if 11 in cardsList and sum(cardsList) > 21:
        cardsList.remove(11)
        cardsList.append(1)
    return sum(cardsList)

def compare(playersScore, computersScore):
  if playersScore > 21 and computersScore > 21:
    return "You went over. You lose 😤"

  if playersScore == computersScore:
    return "Draw 🙃"
  elif computersScore == 0:
    return "Lose, opponent has Blackjack 😱"
  elif playersScore == 0:
    return "Win with a Blackjack 😎"
  elif playersScore > 21:
    return "You went over. You lose 😭"
  elif playersScore > 21:
    return "Opponent went over. You win 😁"
  elif playersScore > computersScore:
    return "You win 😃"
  else:
    return "You lose 😤"    




def playGame():
    playersCards = []
    computersCards = []
    gameOver = False

    for i in range(2):
      playersCards.append(dealCard())
      computersCards.append(dealCard())


    while not gameOver:
        playersScore = calculateScore(playersCards)
        computersScore  = calculateScore(computersCards)
        print(f"   Your cards: {playersCards}, current score: {playersScore}")
        print(f"   Computer's first card: {computersCards[0]}")

        if playersScore == 0 or computersScore == 0 or playersScore > 21:
            gameOver = True
        else:
            userDeal = input("Type 'y' to get another card, type 'n' to pass: ")

            if userDeal == 'y':
                playersCards.append(dealCard())
            else:
                gameOver = True
    while computersScore != 0 and computersScore < 17:
        computersCards.append(dealCard())
        computersScore = calculateScore(computersCards)

    print(f"   Your final hand: {playersCards}, final score: {playersScore}")
    print(f"   Computer's final hand: {computersCards}, final score: {computersScore}")
    print(compare(playersScore, computersScore))    
  


while input("Do you want to play a game of Blackjack? Type 'y' of 'n': ") == "y":
    playGame()

'''

# from audioop import add
# import random

# def blackJack():
#     global listOfCards
#     winner = ""
#     gameStart = input("Do you want to play a game Blackjack? Type 'y' or 'n' ").lower()
#     if gameStart == "n":
#         return
#     elif gameStart == "y":
#         playersCards = []
#         for i in range(2):
#             addCard = random.choice(listOfCards)
#             playersCards.append(addCard)
#         print(f"Your cards: [{playersCards[0]}, {playersCards[1]}], current score : {sum(playersCards)}")



#         computersCards = []



# DAY 12

################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 5
#   return enemies + 1


# enemies = increase_enemies()

# print(enemies)

# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
  


# DAY 13

# for number in range(1, 101):

#   if number % 5 == 0 and number % 3 == 0:
#     print("FizzBuzz") 
#   elif number % 3 == 0 and number % 5 != 0:
#     print("Fizz")
#   elif number % 5 == 0 and number %3 != 0:
#     print("Buzz")
#   else:
#     print([number])


#  DAY 14

# import random
# import os
# import lower_higher_art
# from lower_higher_data import data

# gameGoOn = True
# score = 0
# tempList = []

# def checkScore (playersGuess, aScore, bScore):
#   if playersGuess == "a" and aScore > bScore:
#     return "correct a"
#   elif playersGuess == "b" and bScore > aScore:
#     return "correct b"
#   else:
#     return "incorrect"

# while gameGoOn:  
#   if score == 0:
#     print(lower_higher_art.logo)
#     upperLim = 2
#   else: upperLim == 1
#   for i in range(0, upperLim):  
#     randIndex = random.randint(0, len(data)-1)
#     tempList.append(data[randIndex])
#     data.remove(data[randIndex])

#   print(f"Compare A: {tempList[0]['name']}, a {tempList[0]['description']}, from {tempList[0]['country']}")
#   print(lower_higher_art.vs)
#   print(f"Agaist B: {tempList[1]['name']}, a {tempList[1]['description']}, from {tempList[1]['country']}")
  
#   aScore = tempList[0]['follower_count']
#   bScore = tempList[1]['follower_count']

#   print(aScore)
#   print(bScore)

#   playersGuess = input("Who has more followers? Type 'A' of 'B':").lower()

#   if checkScore(playersGuess, aScore, bScore) == "correct a":
#     score += 1
#     os.system('cls')
#     print(f"Your are right! Current score: {score}") 
#     tempList.remove(tempList[1])
#   elif checkScore(playersGuess, aScore, bScore) == "correct b":
#     score += 1
#     os.system('cls')
#     print(f"Your are right! Current score: {score}") 
#     tempList[0] = tempList[1]
#     tempList.remove(tempList[1])
#   else:
#     score = 0
#     print(f"Sorry that is wrong. Final score: {score}")
#     gameGoOn = False



  # DAY 15

'''
Full tank
Water: 300 ml
Milk: 200 ml
Cofee: 100 g
Money: 0$

quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

'''
# TODO Money handling function
# TODO Ingredients handling function
# TODO Drink preparation function
# TODO General cycle of the program

# from random import choices

trig = True

resources = {'water':300, 'milk': 200, 'coffee': 100}
drinksList = ("espresso", "latte", "cappuccino")
moneyCounter = 0

menu = {"espresso": {}}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def checkResources(drink): # this func checks if resources are sufficient to make ordered drink
  for i in drink:
    if drink[i] > resources[i]:
      return (i)
  return True

def paymentFunc(): # this function handles payment procedure
  # remark: quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01  
  amount = int(input("how many quarters?: "))*0.25
  amount += int(input("how many dimes?: "))*0.1
  amount += int(input("how many nickles?: "))*0.05
  amount += int(input("how many pennies?: "))*0.01
  return amount    

def prepareDrink(drink):# this func is responsible for drink preparing
  choice = MENU[drink]["ingredients"]
  for i in choice:   
    resources[i] = resources[i] - choice[i]    
  return (f"Here is your {drink}. Enjoy!") 
    

  
while trig: # main loop of the program
  userIn = input(f"What would you like? ({drinksList[0]}/{drinksList[1]}/{drinksList[2]}): ").lower()
  if userIn == "off":    
    trig = False    
  elif userIn == "report":
    print(resources)
    print(f"Money: {moneyCounter}")

    continue
  elif userIn not in drinksList:
    raise Exception("Entered name of drink is not correct !!!")
  else:
    drink = MENU[userIn]
    check = checkResources(drink["ingredients"])
    if check == True: # call resousces check func    
      moneyPaid = paymentFunc() # call payment handling func
      if moneyPaid > drink["cost"]:
        change = moneyPaid - drink["cost"]
        print(f"Here is ${change} in change.")
        moneyCounter += drink["cost"] 
        print(prepareDrink(userIn)) # call drink prepare func        
      elif moneyPaid == drink['cost']:
        moneyCounter += drink["cost"]
        print(prepareDrink(userIn))  # call drink prepare func      
      else:
        print("Sorry that's not enough money. Money refunded.")
        moneyPaid = 0
    else:
      print(f"​Sorry there is not enough {check}.")   

  
   
        
# DAY 16






