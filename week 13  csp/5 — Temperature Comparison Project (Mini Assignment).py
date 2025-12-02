# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
todays_temp = int(input('What is the temperature outside?'))
if [-30] < todays_temp < [0]:
    print('Its Freezing!')
elif [0] < todays_temp < [32]:
    print('Its really cold')
elif [32] < todays_temp < [50]:
    print("Its mad Brick out")
elif [50] < todays_temp < [70]:
    print('Its chilly')
elif [70] < todays_temp < [90]:
    print('Its Nice Out')
elif [90] < todays_temp < [120]:
    print('Its Really Hot!')

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

