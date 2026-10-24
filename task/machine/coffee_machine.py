from pkgutil import get_loader
from typing import Any


class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.STATE = "MAIN"

    def system_input(self, user_input):
        if self.STATE == "MAIN" and user_input == "buy":
            self.STATE = "BUY"
        elif self.STATE == "MAIN" and user_input == "fill":
            self.STATE = "FILL_WATER"
        elif self.STATE == "MAIN" and user_input == "take":
            self.STATE = "TAKE"
        elif self.STATE == "MAIN" and user_input == "remaining":
            self.STATE = "REMAINING"
        elif self.STATE == "MAIN" and user_input == "exit":
            self.STATE = "EXIT"
        elif self.STATE == "FILL_WATER":
            self.refill_water(user_input)
            # self.STATE = "FILL_MILK"
        elif self.STATE == "FILL_MILK":
            self.refill_milk(user_input)
            # self.STATE = "FILL_BEANS"
        elif self.STATE == "FILL_BEANS":
            self.refill_beans(user_input)
            # self.STATE = "FILL_CUPS"
        elif self.STATE == "FILL_CUPS":
            self.refill_cups(user_input)
            # self.STATE = "MAIN"


    def __repr__(self):
        # should print how much of each item the coffee machine has
        return(f"""
            The coffee machine has:
            {self.water} ml of water
            {self.milk} ml of milk
            {self.beans} g of coffee beans
            {self.cups} disposable cups
            ${self.money} of money    
        """)

    def __str__(self):
        return (f"""
            The coffee machine has:
            {self.water} ml of water
            {self.milk} ml of milk
            {self.beans} g of coffee beans
            {self.cups} disposable cups
            ${self.money} of money    
                """)

    def return_money(self):

        print(f"I gave you ${self.money}")
        self.money = 0

    def refill_water(self, water):
        self.water += int(water)

    def refill_milk(self, milk):
        self.milk += int(milk)

    def refill_beans(self, beans):
        self.beans += int(beans)

    def refill_cups(self, cups):
        self.cups += int(cups)

    def build_espresso(self):
        """
        For one espresso, the coffee machine needs:
        250mL of water
        16g of coffee beans
        costs $4
        :return:
        """
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        else:
            # print("Cannot make a cup of coffee")
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough beans!")
            if self.cups < 1:
                print("Sorry, not enough cups!")

    def build_latte(self):
        """
        For one latte, the coffee machine needs:
        350mL of water
        75mL of milk
        20g of coffee beans
        costs $7
        :return:
        """

        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        else:
            # print("Cannot make a cup of coffee")
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 20:
                print("Sorry, not enough beans!")
            if self.cups < 1:
                print("Sorry, not enough cups!")


    def build_cappuccino(self):
        """
        200mL of water
        100mL of milk
        12g of coffee beans
        costs $6
        :return:
        """

        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        else:
            # print("Cannot make a cup of coffee")
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough beans!")
            if self.cups < 1:
                print("Sorry, not enough cups!")

if __name__ == '__main__':

    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

    while True:
        user_input = input("Write action (buy, fill, take, remaining, exit): ").strip()
        coffee_machine.system_input(user_input)
        if coffee_machine.STATE == "BUY":
            choose_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ").strip()
            if choose_coffee == "1":
                coffee_machine.build_espresso()
                coffee_machine.STATE = "MAIN"
                continue
            elif choose_coffee == "2":
                coffee_machine.build_latte()
                coffee_machine.STATE = "MAIN"
                continue
            elif choose_coffee == "3":
                coffee_machine.build_cappuccino()
                coffee_machine.STATE = "MAIN"
                continue
            elif choose_coffee == "back":
                coffee_machine.STATE = "MAIN"
        elif coffee_machine.STATE == "FILL_WATER":
            enter_water = input("Write how many mL of water you want to add: ")
            coffee_machine.system_input(enter_water)
            coffee_machine.STATE = "FILL_MILK"
            enter_milk = input("Write how many mL of milk you want to add: ")
            coffee_machine.system_input(enter_milk)
            coffee_machine.STATE = "FILL_BEANS"
            enter_beans = input("Write how many grams of coffee beans you want to add: ")
            coffee_machine.system_input(enter_beans)
            coffee_machine.STATE = "FILL_CUPS"
            enter_cups = input("Write how many cups you want to add: ")
            coffee_machine.system_input(enter_cups)
            coffee_machine.STATE = "MAIN"
            continue
        elif coffee_machine.STATE == "TAKE":
            coffee_machine.return_money()
            coffee_machine.STATE = "MAIN"
            continue
        elif coffee_machine.STATE == "REMAINING":
            print(coffee_machine)
            coffee_machine.STATE = "MAIN"
            continue
        elif coffee_machine.STATE == "EXIT":
            break







