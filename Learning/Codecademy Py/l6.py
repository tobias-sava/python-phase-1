# 10/12/2024 - codecademy practice project "len's slice" 

# exercising lists again

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives",
            "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

# Your boss wants you to do some research on $2 slices.

num_two_dollar_slices = prices.count(2)

# Find the length of the toppings list and store it in a variable called num_pizzas.

num_pizzas = len(toppings)

print(f"We sell {num_pizzas} different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"],
                    [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]


pizza_and_prices.pop()

pizza_and_prices.insert(3, [2.5, "peppers"])

pizza_and_prices.sort()

print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

three_cheapest = pizza_and_prices[:3]

print(three_cheapest)

# boring






