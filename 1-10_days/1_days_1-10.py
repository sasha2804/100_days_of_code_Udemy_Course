# in1 = input("Welcome to the Band Name Generator \nWhat is name of the city you grew up in? ")
# in2 = input("What is your pet's name? ")
# print("Your band name can be either %s or %s"%(in1, in2))

# print("part1" + "part2")
# print('print("123"+"456")')

# x = "4564"

# print("Hello " + input("Enter your name: ") + "!" + x)

# print(type(input("what is your name?")))

'''

'''

# numChar = len(input("What is your name?"))

# print("Your name has got " + str(numChar) + " characters")

# print(type(numChar))

# Integer

# Float

# String

# Boolean

# a = 123.2

# print(type(a))

# 🚨 Don't change the code below 👇1,8

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI = float(weight)/(float(height))
# print(round(float(weight)/(float(height)**2),2))


# F-string


# 🚨 Don't change the code above 👆

# age = int(input("What is your current age?"))
# days = (90 - age)*365
# weeks = (90 - age) * 52
# months = (90 - age) * 12

# print(f"You have {days} days, {weeks} weeks, {months} months left")


# age = (input("What is your current age?"))
# years = 90 - int(age)
# print(f"You have {years*365} days, {years*52} weeks, {years*12} months left")



# print("Welcome to the tip calculator!")
# tipOption = {.10,.12,.15}
# totalBill = int(input("What was the total bill? $"))
# tipAmountPerc = int(input("How much tip would you like to give? 10,12, or 15?"))/100

# while tipAmountPerc not in tipOption:
#     tipAmountPerc = int(input("Enter correct value of the tip? It can be 10,12, or 15?"))/100
    
# qtyOfPeople = int(input("Who many people to split the bill?"))
# eachPersPay = round(totalBill*(1+tipAmountPerc)/qtyOfPeople, 2)
# print(f"Each person should pay: ${eachPersPay}")1


# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI = round(float(weight)/(float(height)*float(height)))


# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")


# year = 1999
# if year%4 != 0:
#     print("Not leap")
# elif year%100 != 0:
#     print("Leap")
# elif year%400 == 0:
#     print("Leap")
# else:
#     print("Not leap")

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# name1 = name1.lower()
# name2 = name2.lower()

# keyWord1 = 'true'
# keyWord2 = 'love'
# score1 = 0
# score2 = 0
# scoreFinal = 0

# for i in name1+name2:
#     score1 += keyWord1.count(i)

# for i in name1 + name2:
#     score2 += keyWord2.count(i)

# scoreFinal = score1*10 + score2

# if scoreFinal < 10 or scoreFinal > 90:
#     print(f"Your score is {scoreFinal}, you go together like coke and mentos.")
# elif 40 <= scoreFinal <= 50:
#     print(f"Your score is {scoreFinal}, you are alright together.")
# else:
#     print(f"Your score is {scoreFinal}.")



# speech = "She said: Hi"
# # speech = "She said: \"Hi\""
# print(speech)




# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 


# step1= input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if step1 == "left":
#     step2 = input('You\'ve come to a lake. There is an island in the middle of the lake. \
#         Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#     if step2 == "wait": 
#         step3 = input("You arrive at the island unharmed. There is a house with 3 doors. \
#             One red, one yellow and one blue. Which colour do you choose? \n").lower()
#         if step3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif step3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif step3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist")
#     else:
#         print("Attacked by trout. Game over.")
# else:
#     print("You fell into a hole. Game over.")



# import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)


# result = random.randint(0,1)

# if result == 1:
#     print("Heads")
# else:
#     print("Tails")

# x = -2

# newlist = [x for x in range(10) if x%2==0]

# print(newlist)

# Angela, Ben, Jenny, Michael, Chloe

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# # print(len(names))
# # print(type(names))

# import random
# PersonNr = random.randint(0, len(names)-1)
# print(names[PersonNr])


# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map1 = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# column = int(position[1])
# row = int(position[0])
# map1[column-1][row-1] = "x"
# for i in map1:
#     print(i)

# user = "scissors"
# computer = "paper"

# from multiprocessing import parent_process
# import random

# list1 = ["user", "computer"]

# userInput = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors." )





# if userInput == 0:
#     list1[0] = "rock"
# elif userInput == 1:
#     list1[0] = "paper"
# else:
#     list1[0] = "scissors"


# computerInput = random.randint(0,3)
# if computerInput == 0:
#     list1[1] = "rock"
# elif computerInput == 1:
#     list1[1] = "paper"
# else:
#     list1[1] = "scissors"


# if list1[0] != list1[1]:
#     # case 1
#     if "scissors" in list1 and "paper" in list1:
#         if list1.index("scissors") == 0:
#             print("You won")
#         else:
#             print("PC won")

#     # case 2
#     if "rock" in list1 and "scissors" in list1:
#         if list1.index("rock") == 0:
#             print("You won")
#         else:
#             print("PC won")

#     # case 3
#     if "paper" in list1 and "rock" in list1:
#         if list1.index("paper") == 0:
#             print("You won")
#         else:
#             print("PC won")
# else:
#     print("There is no winner")
    

# print(f"\nuser input: {list1[0]}")
# print(f"pc input: {list1[1]}")




# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# imagesList = [rock, paper, scissors]

# userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. " ))
# inputsList = {0, 1, 2}

# # print(inputsList)

# while userInput not in inputsList:
#     userInput = int(input("!!! What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. " ))
#     if userInput in inputsList:
#         break

# print("User chooses:")
# print(imagesList[userInput])

# pcInput = random.randint(0,2)
# # print("pc input: ",pcInput)
# print("Computer chooses:")
# print(imagesList[pcInput])

# if userInput == pcInput:
#     print("Draw")
# else:
#     if userInput == 0 and pcInput == 2:
#         print("You won")
#     elif userInput == 2 and pcInput == 0:
#         print("PC won")
#     elif userInput == 2 and pcInput == 1:
#         print("You won")
#     elif userInput == 1 and pcInput == 2:
#         print("PC won")
#     elif userInput == 1 and pcInput == 0:
#         print("You won")
#     elif userInput == 0 and pcInput == 1:
#         print("PC won")
    

# 180, 124, 165, 173, 189, 169, 146

# student_heights = input("Input a list of student heights ").split(",")
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])


# print(round(sum(student_heights)/len(student_heights)))

# sumHeights = 0
# for i in student_heights:
#     sumHeights += i   
# print(round(sumHeights/len(student_heights)))

# 78, 65, 89, 86, 55, 91, 64, 89

# student_scores = input("Input a list of student scores ").split(",")
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# maxScore = student_scores[0]

# for i in student_scores:
#     if i > maxScore:
#         maxScore = i

# print(f"The highest score in the class is: {maxScore}")


# total = 0
# for i in range(2, 101, 2):
#     total += i
# print(total)

# for i in range(1, 101):
#     if i%3==0 and i%5==0:
#         message = "FizzBuzz"
#     elif i%3==0:
#         message = "Fizz"
#     elif i%5==0:
#         message = "Buzz"
#     else:
#         message = i
#     print(message)


# method 1
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# tempList = []
# passString = ""

# for i in range(nr_letters):
#     position = random.randint(0, len(letters)-1)
#     tempList.append(letters[position])

# for i in range(nr_numbers):
#     position = random.randint(0, len(numbers)-1)
#     tempList.append(numbers[position])

# for i in range(nr_symbols):
#     position = random.randint(0, len(symbols)-1)
#     tempList.append(symbols[position])

# while len(tempList) != 0:
#     position = random.randint(0, len(tempList)-1)
#     passString += tempList[position]
#     tempList.remove(tempList[position])

# print(passString)


# method 2
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# passList = []
# passString = ""

# for i in range(nr_letters):
#     passList.append(random.choice(letters))

# for i in range(nr_numbers):
#     passList.append(random.choice(numbers))

# for i in range(nr_symbols):
#     passList.append(random.choice(symbols))

# random.shuffle(passList)

# for i in passList:
#     passString += i

# print(passString)


#   DAY 7 
# import random
# from hangman_words import word_list
# from hangman_art import stages
# from hangman_art import logo

# #Step 1 
# endOfGame = False
# qtyOfLives = 6

# print(logo)
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosenWord = random.choice(word_list)
# print(f"Chosen word is {chosenWord}")
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# listGuesLett = ["_" for i in range(len(chosenWord))]

# while not endOfGame:
#     guessLetter = input("Make a guess letter ").lower()
#     for i in range (len(chosenWord)):
#         letter = chosenWord[i]
#         if guessLetter == letter:
#             listGuesLett[i] = guessLetter
    
#     if guessLetter not in chosenWord:
#         qtyOfLives -= 1
#         if qtyOfLives == 0:
#             endOfGame = True
#             print("You lost")
#     print(f" ".join(listGuesLett))

#     if "_" not in listGuesLett:
#         endOfGame = True
#         print("You won.")
#     print(stages[qtyOfLives])

# def paint_calc(width, height, coverage):
#     numberOfCans = round((height * width)/coverage)
#     print(f"You'll need {numberOfCans} cans of paint.")
    
# coverage = 5
# height = 2
# width = 4

# paint_calc(width, height, coverage)




'''
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# direction = "encode"
# text = "prime"
# text = "qsjnf"
# direction = "decode"

# direction = "encode"
# text = "civilization"

#direction = "decode"
#text = "jpcpspghapvu"
 

# direction = "encode"
# text = "prime"

#shift = 85
#str1 = ""

def encode(text, shift):
    global str1
    for i in text:
        newPos = alphabet.index(i) + shift
        if newPos >= len(alphabet):
            shiftMult = newPos//len(alphabet)
            newPos = newPos - len(alphabet)*shiftMult            
        str1 += alphabet[newPos]       

def decode(text, shift):
    global str1
    for i in text:
        newPos = alphabet.index(i) - shift
        if (shift + alphabet.index(i)) > len(alphabet):
            shiftTemp = shift - alphabet.index(i)
            newPos = shiftTemp%len(alphabet)*(-1)        
        str1 += alphabet[newPos]


if direction == "encode":
    encode(text, shift)
elif direction == "decode":
    decode(text, shift)
    
print(str1)


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
'''
'''
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

programFlow = "yes"
trigger = True

def caesar(text, shift, direction):
    str1 = ""
    if direction == "encode":
        for i in text:
            if i not in alphabet:
                str1 += i
            else: 
                newPos = alphabet.index(i) + shift
                if newPos >= len(alphabet):
                    shiftMult = newPos//len(alphabet)
                    newPos = newPos - len(alphabet)*shiftMult            
                str1 += alphabet[newPos]        

    elif direction == "decode":
        for i in text:
            if i not in alphabet:
                str1 += i
            else:
                newPos = alphabet.index(i) - shift
                if (shift + alphabet.index(i)) > len(alphabet):
                    shiftTemp = shift - alphabet.index(i)
                    newPos = shiftTemp%len(alphabet)*(-1)        
                str1 += alphabet[newPos]
    
    return(f'Here is the {direction}d result: {str1}')


while trigger:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(caesar(text, shift, direction)) 

    programFlow = input('Type "yes" if you want to go again. Otherwise type "no": ')
    if programFlow == "no":
        break
'''

# DAY 9
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


# 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# #TODO-2: Write your code below to add the grades to student_grades.👇
# for x, y in student_scores.items():
#     if  100 >= y >= 91:
#         y = "Outstanding"
#     elif 90 >= y >= 81:
#         y =  "Exceeds Expectations"
#     elif 80 >= y >= 71:
#         y = "Acceptable"
#     elif y <= 70:
#         y = "Fail"
    
#     student_grades[x] = y
   

# # 🚨 Don't change the code below 👇
# print(student_grades)

# nested dictionary


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[key] += 1

print(dict)

'''


from asyncio.streams import FlowControlMixin
from http.client import NOT_EXTENDED
from itertools import count
from math import fabs


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


'''
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


def add_new_country(countryName, nrOfVisits, cities):
    global travel_log
    travel_log.append({"country": countryName, "visits": nrOfVisits, "cities": cities})
 
#thisdict["color"] = "red"

#🚨 Do not change the code below
add_new_country("Ukraine", 12, ["Kyiv", "Kharkiv", "Odessa"])
add_new_country("Germany", 2, ["Berlin", "Rostok", "Stuttgart"])

print(travel_log)
'''

'''

import os
import art

print(art.logo)
print("Welcome to the secret auction program.")
bid = dict()
trigger = True   


while trigger:
    name = input("What is your name?: ")
    bidAmount = int(input(("What is your bid?: $")))
    bid[name] = bidAmount
    bidders = input('Are there any other bidders, Type "yes" or "no": ').lower()

    if bidders == "no":        
        k = list(bid.keys())  #keys list       
        v = list(bid.values()) #values list       
        maxVal = max(v)
        ind = v.index(maxVal)
        nameWinner = k[ind]
        os.system('cls') #clear console for the next bidder
        print(f"The is winner is {nameWinner} with a bid ${maxVal}")
        break            
    os.system('cls') #clear console for the next bidder

'''

# DAY 10

'''
def format_name(f_name, l_name):
    
    return(f_name.title(), l_name.title())


print(format_name("alex", "cooper"))
# print(format_name("",""))
'''


# year = 1999
# if year%4 != 0:
#     print("Not leap")
# elif year%100 != 0:
#     print("Leap")
# elif year%400 == 0:
#     print("Leap")
# else:
#     print("Not leap")


'''
def is_leap(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 == 0:
        return True 
    else:
        return False 


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    
    if month < 12 and month >= 1 and len(str(year)) <= 4:
        if month == 2 and is_leap(year):
            return (month_days[month-1] + 1)             
        return(month_days[month-1])  
    else:
        raise Exception("Input is not correct   ")

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
'''

# DAY 10 calculator method 1

# import os
# result = 0
# trigger = True
# trigger1 = True


# while trigger:
#     if result == 0:
#         firstNum = float(input("What's the first number?: "))
#     operationSymb = (input('''+\n-\n*\n/\nPick an operation: '''))
#     nextNum = float(input("What's the next number?: "))

#     resultTemp = result

#     if operationSymb == "+":
#         result = result + firstNum + nextNum
#     elif operationSymb == "-":
#         result = (result + firstNum) - nextNum
#     elif operationSymb == "*":
#         result = (result + firstNum) * nextNum
#     else:
#         result = (result + firstNum)/nextNum    

#     if trigger1 == True:
#         combinedNum = firstNum
#     else:
#         combinedNum = resultTemp

#     print(f"{combinedNum} {operationSymb} {nextNum} = {result}")
#     trigger1 = False

#     programFlow = input(f"Type 'y' to continue calculation with  {result}, or type 'n' to start a new calculation: ")

#     if programFlow == "n":
#         result = 0
#         firstNum = 0
#         nextNum = 0
#         trigger1 = True
#         os.system('cls') #clear console for the next operation
#     elif programFlow == "y":
#         firstNum = 0
 
    
# DAY 10 calculator method 2

import os
from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operationsList = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

trigger = True

def calculatorStart():  
    print(logo)

    firstNum = float(input("What's the first number?: "))
    for i in operationsList:
        print(i)

    trigger = True

    while trigger:
        operation = input("Pick an operation: ")
        nextNum = float(input("What's the next number?: "))
        calcFunc = operationsList[operation]
        result = calcFunc(firstNum, nextNum)
        print(f"{firstNum} {operation} {nextNum} = {result}")

        flow = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if flow == "y":
            firstNum = result
        else:
            trigger = False
            os.system('cls')
            calculatorStart()
            
    
calculatorStart()


























     