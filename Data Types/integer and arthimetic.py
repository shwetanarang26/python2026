integer and arthimetic.py
# Shopping Calculator
print("Running 'Shopping Calculator App':")
wallet = 50  # You start with 50$
# Buy Some Items
book = 15
snack = 5
drink = 3
hat = 12
# Calculate total spent
total_spent = book + snack + drink + hat
# Calculate remaining money
money_left = wallet - total_spent

number_of_items = 4
average_cost = total_spent / number_of_items

print("You spent in $", total_spent)
print("You have in $", money_left, "left")
print("Average cost of all item in $", average_cost)

# Task: 
# 1. Add one more item to buy
# 2. Calculate the average cost of all items.
