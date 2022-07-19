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


year = 1999
if year%4 != 0:
    print("Not leap")
elif year%100 != 0:
    print("Leap")
elif year%400 == 0:
    print("Leap")
else:
    print("Not leap")






