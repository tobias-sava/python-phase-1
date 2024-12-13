# 13/12/2024 - codecademy "python code challenges: functions"

# i have already done like 20 of these but i didnt think of solving them in this repo :/
import math
# 1 - tenth power

def tenth_power(num):
    return num ** 10

# correct

# 2 - square root

def square_root(num):
    #return math.sqrt(num) - nevermind, cant import modules in their IDE
    return num ** 0.5

# correct

# 3 - win percentage

def win_percentage(wins, losses):
    total = wins + losses
    ratio = total - wins
    perc = ratio * 10
    return perc

# wrong, only works if neither parameters include 0!

# correct resolution below

def win_percentage(wins, losses):
    total_games = wins + losses
    ratio_won = wins / total_games
    return ratio_won * 100

# 4 - average 

# CONTINUE HERE