# 9/12/2024 - codecademy project "magic 8-ball"

# making me create a simple terminal-based 8-ball program

# this is my take on creating it without any guidance

# ill start by listing the answers
# ill also need the random module to randomly pick a reply for the 8-ball

import random

possible_answers = ["Yes - definitely", "It is decidedly so", "Without a doubt",
                    "Reply hazy, try again", "Ask again later", "Better not tell you now"
                    "My sources say no", "Outlook not so good", "Very doubtful"]

print("Welcome to the 8-ball game.")
name = input("What is your name? ")

question = input("What would you like to ask the 8-Ball? ")

answer = random.choice(possible_answers)

print(f"[{name}] asks: {question}")
print(f"Magic 8-Ball's answer: {answer}")

# thats about it lol

# here's the code they had as the solution
# it is longer because their IDE does not support the input function i think.

import random

name = "Joe"
question = "Will I win the lottery?"
answer = ""

random_number = random.randint(1, 9)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
  
print(name + " asks: " + question)
print("Magic 8 Ball's answer: " + answer)