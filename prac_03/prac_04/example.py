# Using the format method:
# month = int(input("Enter the month number ({}-{}): ".format(MINIMUM_MONTH, MAXIMUM_MONTH)))

# Using string concatenation and explicit type conversion
# month = int(input("Enter the month number (" + str(MINIMUM_MONTH) + "-" + str(MAXIMUM_MONTH) + "): "))

# Using f-strings
# month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

# CODE FIX
# Constants for month-related values
MIN_MONTH = 1
MAX_MONTH = 12
HALF_YEAR = 6

# Get user input for the month
month = int(input(f"Enter the month number ({MIN_MONTH}-{MAX_MONTH}): "))

# Validate input
while month < MIN_MONTH or month > MAX_MONTH:
    print("Invalid input. Month should be between 1 and 12.")
    month = int(input(f"Enter the month number ({MIN_MONTH}-{MAX_MONTH}): "))

# Determine the half of the year
if month <= HALF_YEAR:
    half = "first"
else:
    half = "second"

# Print the result
print(f"The birth month is in the {half} half of the year.")
