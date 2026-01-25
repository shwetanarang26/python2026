x = 42
y = -100
result = x + y * 2
print(result)
# Take input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest is:", simple_interest)

Total_amount = simple_interest + principal

print("Total_amount is:", Total_amount)

# Calculate compound amount
amount = principal * (1 + rate / 100) ** time

# Calculate compound interest
compound_interest = amount - principal

# Display result
print("Compound Interest is:", compound_interest)
print("Total Amount is:", amount)

