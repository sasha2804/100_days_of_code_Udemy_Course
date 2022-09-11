# DAY 16

from menu_day_16 import Menu, MenuItem
from coffee_maker_day_16 import CoffeeMaker
from money_machine_day_16 import MoneyMachine

maker = CoffeeMaker()
menu = Menu()
# menuItem = MenuItem()
moneyMachine = MoneyMachine()

trig = True

while trig:
    listOfItems = menu.get_items()
    userInput = input(f"What would you like ? ({listOfItems}): ")
    if userInput == "off":
        break
    elif userInput == "report":
        maker.report()        
    else:
        drink = menu.find_drink(userInput)
       
        if maker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            maker.make_coffee(drink)


        

        


        


    
    
  






