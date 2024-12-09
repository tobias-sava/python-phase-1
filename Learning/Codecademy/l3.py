# 9/12/2024 - codecademy project "sal's shipping"

# calculates shipping cost of x package

# i will follow the codecademy tutorial for this, even though i could do it on my own

weight = 1.5

# ground shipping

if weight <= 2:
    p1 = 1.50
elif weight <= 6:
    p1 = 3.00
elif weight <= 10:
    p1 = 4.00
else:
    p1 = 4.75

ground_flat_charge = 20

ground_final_charge = weight * p1 + ground_flat_charge

ground_premium_charge = 120

# drone shipping

if weight <= 2:
    p2 = 4.50
elif weight <= 6:
    p2 = 9.00
elif weight <= 10:
    p2 = 12.00
else:
    p2 = 14.25

drone_final_charge = weight * p2

print(drone_final_charge)

# passed tests

# i will make my own version below real quick

print("Welcome to Sal's Shipping calculator.")

weight = input("Please input the weight of your package: ")

method = input("Please type 'g' for ground shipping or 'd' for drone shipping: ")

if method == 'g':
    if weight <= 2:
        p1 = 1.50
    elif weight <= 6:
        p1 = 3.00
    elif weight <= 10:
        p1 = 4.00
    else:
        p1 = 4.75

# formula for calculating final price (last int is the flat charge)
    
result1 = weight * p1 + 20
    
print(f"Amount due for package weighing {weight} via Ground Shipping is {result1}.")

# doesnt work and im too hungry to google-shoot