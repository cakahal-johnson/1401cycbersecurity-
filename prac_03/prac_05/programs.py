# prac_05
# Input, Processing, Output
# 1. Percentage change

# Input: Ask the user for the original value and the percentage change
get_original_value = float(input("Enter the original value: "))
percentage_change = float(input("Enter the percentage change (positive for increase: "))

# Processing: Calculate the new value
# Calculate increase
new_value = get_original_value * (1 + percentage_change)

# Output: Print the original value, percentage change, and the new result
print(f"Original: {get_original_value}, Change: {percentage_change}, Result: {new_value}")


# 2. Time of day

# Input: Ask the user for the time of day and if they are coming or going
time_of_day = int(input("Enter the time of day (0-23 hours): "))
state = input("Coming or going? ").lower()

# Processing: Determine the appropriate statement based on user inputs
if time_of_day < 12:
    noon_message = "before"
else:
    noon_message = "after"
if state == "coming":
    direction_message = "coming. Hi!"
else:
    direction_message = "going. Bye!"

# Output: Print the single customized output statement
print(f"It is {noon_message} noon and you are {direction_message}")


# 3. Coffee orders

# Input: Ask the user for the type and size of coffee
coffee_colour = input("Do you want white or black coffee? ").lower()
coffee_size = input("Choose the size (small, medium, or large): ").lower()

# Processing: Determine the cost based on user inputs
if coffee_size == "small":
    cost = 3
elif coffee_size == "medium":
    cost = 4
else:
    cost = 5
if coffee_colour != "black":
    cost += 1
print("${}".format(cost))


# Repetition Structures
# 4. Coffee orders with error-checking
coffee_colour = input("Colour: ").lower()
while coffee_colour != "black" and coffee_colour != "white":
    print("Invalid input")
    coffee_colour = input("Colour: ").lower()

coffee_size = input("Size: ").lower()
while coffee_size != "small" and coffee_size != "medium" and coffee_size != "large":
    print("Invalid input")
    coffee_size = input("Size: ").lower()


if coffee_size == "small":
    cost = 3
elif coffee_size == "medium":
    cost = 4
else:
    cost = 5
if coffee_colour != "black":
    cost += 1
print("${}".format(cost))


# 5. Accumulation
low_value = int(input("Enter a Low value: "))
high_value = int(input("Enter a High value: "))

while high_value < low_value:
    print("High must be >=", low_value)
    high_value = int(input("High: "))
total = 0
for i in range(low_value, high_value + 1):
    print(i, end=" ")
    total += i
print("totals:", total)


# 6. Debugging
# age = int(input("Age: "))
# if age < 18:
#     print("Entry refused")
# elif age < 30:
#     print("Limited entry allowed")
# elif age > 30:
#     print("Full entry allowed")

# Test values:
age = int(input("Age: "))
if age < 18:
    print("Entry refused")
elif 18 <= age < 30:
    print("Limited entry allowed")
else:
    print("Full entry allowed")

# Added elif 18 <= age < 30: to ensure that the second condition is only checked if the age is not less than 18.
# This ensures exclusivity between conditions.
"""
Test values:

Test with age < 18:

Input: 16
Expected outcome: "Entry refused"
Test with 18 <= age < 30:

Input: 22
Expected outcome: "Limited entry allowed"
Test with age >= 30:

Input: 35
Expected outcome: "Full entry allowed"
Test with edge case, age = 18:

Input: 18
Expected outcome: "Limited entry allowed"
Test with edge case, age = 30:

Input: 30
Expected outcome: "Full entry allowed"
By testing these values, we can verify that the code handles all possible scenarios correctly.
"""