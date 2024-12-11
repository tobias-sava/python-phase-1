# 11/12/2024 - codecademy practice project "carly's clippers"

# data given by codecademy:

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# i will be following and completing relevant exercises from codecademy

# task 1

total_price = 0

for x in prices:
    total_price += x

print(total_price)

average_price = total_price / len(prices)

print(average_price)

print(f"Average Haircut Price: {average_price}")

new_prices = [price - 5 for price in prices]

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
    
print(f"Total Revenue: {total_revenue}")

average_daily_revenue = total_revenue / 7

print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)

# all tests passed

# maybe i should start commenting individual code pieces and explain their functionality

# bye