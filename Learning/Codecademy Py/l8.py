# 12/12/2024 - codecademy practice "parameters and arguments"

# i already know a bit about functions but this is a good recap

# creating program that generates directions for user trips

# creating trip instruction function

def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)

generate_trip_instructions("Central Park")

# ok nevermind that was literally the whole exercise ...

# next lesson - multiple parameters

# had to do it on codecademy because i need to use their on-site IDE ...

# built in functions vs user defined functions lesson got me thinking.
# i now feel like i understand functions better :)

# code from codecademy exercise below

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:

# Checkpoint 1
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

# Checkpoint 2
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

# Checkpoint 3
rounded_price = round(tshirt_price, 1)
print(rounded_price)

# codecademy function practice:

# Write your code below:

def trip_planner_welcome(name): 
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome(" <YOUR NAME HERE> ")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")


destination_setup(" <PICK AN ORIGIN> ", "<PICK A DESTINATION > ", estimate, "Car")

