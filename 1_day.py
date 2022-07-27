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


import random

random_float = random.random()


print(random_float*5)






