import os

available_pizzas = ['margarita', 'pollo', '4cheese', 'bolognese', 'vegetarian']
available_toppings = ['mushroom', 'onions', 'green pepper', 'extra cheese']
pizza_prices = {'margarita': 5, 'pollo': 7, '4cheese': 6, 'bolognese': 8, 'vegetarian': 6.5}
topping_prices = {'mushroom':1, 'onions': 2, 'green pepper':3, 'extra cheese':4}

def ShowMenu():
    os.system('cls')
    print("Available Pizzas:\n")
    print(*available_pizzas,sep = ', ')
    print("\n\nAvailable Topings:\n")
    print(*available_toppings,sep = ', ')
    print('\n\n')

def TakeOrderInput():
    os.system('cls')
    print("Hi, welcome to our text based pizza ordering")
    ordering = True
    while ordering:
        os.system('cls')
        ShowMenu()
        pizza = input("Please choose a pizza: ")
        if pizza not in available_pizzas:
            print(f"I am sorry, we currently do not have {pizza}\n.")
            os.system('pause')
            continue
        topping = input("Please choose a topping: ")
        if topping not in available_toppings:
            print(f"I am sorry, we currently do not have {topping}\n.")
            os.system('pause')
            continue

        print(f"Final order: {pizza} with topping {topping}: ")
        ordering = False

    return pizza,topping

class Order:
    def __init__(self):
        taxes = 0 #You can add taxes
        pizza,topping = TakeOrderInput()
        self.type = pizza
        self.topping = topping
        self.PizzaPrice = pizza_prices[pizza]
        self.ToppingPrice = topping_prices[topping]
        self.Total = self.PizzaPrice + self.ToppingPrice





choice = True
orders = []
orderchoice = input("Welcome! Would you like to order ? (y/n): ")
if orderchoice == 'n':
    print("Have a nice day!")
else:
    while choice:
        neworder = Order()
        orders.append(neworder)
        newchoice = input("Would you like to order again? (y/n): ")
        if (newchoice) == 'n':
            break

total = 0
for order in orders:
    total+=order.Total

print("Total: ",total, '$')