# 1. Tax

# Pseudocode for Python Party Tax Program

# Constants
TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

# Input
income = float(input("Enter your income: $"))

# TODO code:
# Using decision pattern to determine the tax category
if income < TAX_THRESHOLD_LOW:
    # No tax for income under $100
    total_tax_rate = 0
elif income <= TAX_THRESHOLD_HIGH:
    # 5% tax for income between $100 and $1000
    total_tax_rate = income * TAX_RATE_LOW
else:
    # 10% tax for income over $1000
    total_tax_rate = income * TAX_RATE_HIGH

# Calculate take-home pay
take_home_pay = income - total_tax_rate

# Output
print("Total tax is: $", total_tax_rate, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# ================================= end of Task 1. Tax ==========================================

# Car Insurance
# Pseudocode for Car Insurance Program

# Constants
AGE_THRESHOLD_REFUSED = 18
AGE_THRESHOLD_SPECIAL_INSURANCE = 25

# Input
age = int(input("Enter your age: "))

# TODO: Check the age and determine insurance requirement
# Use decision structure to evaluate different age categories
if age < AGE_THRESHOLD_REFUSED:
    # Applicants under 18 are refused hire
    output_message = "Hire refused"
elif age < AGE_THRESHOLD_SPECIAL_INSURANCE:
    # Applicants under 25 are required to purchase special insurance
    output_message = "Insurance required"
else:
    # Applicants 25 years and over are not required to purchase insurance
    output_message = "Insurance not required"

# Output
print(output_message)

# =============================== end of Task 2. Car Insurance ===========================================

# 3. Simple Password Checker
# Pseudocode for Simple Password Checker Program

# Constants
SECRET_PASSWORD = "mySecretPassword"

# Input
user_password = input("Enter your password: ")

# TODO: Check user's password against the secret password
# Use string comparison to determine access status
if user_password == SECRET_PASSWORD:
    output_message = "Access granted"
else:
    output_message = "Access denied"

# Output
print(output_message)

# =================================== end of Task 3. Simple Password Checker =======================

# 4. Dog Years
# Pseudocode for Dog Years Program

# Constants
DOG_YEARS_FIRST_TWO_HUMAN_YEARS = 10.5
DOG_YEARS_PER_HUMAN_YEAR_AFTER_TWO = 4

# Input
human_years = int(input("Enter the age in human years: "))

# TODO: Calculate the dog's age in dog years
if human_years <= 2:
    dog_years = human_years * DOG_YEARS_FIRST_TWO_HUMAN_YEARS
else:
    dog_years = 2 * DOG_YEARS_FIRST_TWO_HUMAN_YEARS + (human_years - 2) * DOG_YEARS_PER_HUMAN_YEAR_AFTER_TWO

# Output
print("Age in human years:", human_years)
print("Age in dog years is", dog_years)

# ============================================= end of Task 4. Dog Years ======================================

# 5. Rock of Ages Program
# Pseudocode for Rock of Ages Program

# Constants
MINIMUM_AGE = 0
MAXIMUM_AGE = 120

# Input
user_age = int(input("Enter your age: "))

# TODO: Check if the age is invalid
if user_age < MINIMUM_AGE or user_age > MAXIMUM_AGE:
    print("Invalid age")
else:
    # TODO: Determine age category and provide a custom response
    if user_age <= 12:
        print("You're in the 'Childhood' age category.")
    elif user_age <= 19:
        print("You're in the 'Teenager' age category.")
    elif user_age <= 35:
        print("You're in the 'Young Adult' age category.")
    else:
        print("You're in the 'Adult' age category.")


# ============================ end of Task 5. Rock of Ages Program ====================================

# 6. Speeding Fines
# Pseudocode for Speeding Fines Program

# Constants
FINE_THRESHOLD_1 = 11
FINE_THRESHOLD_2 = 20
FINE_THRESHOLD_3 = 30
FINE_THRESHOLD_4 = 40

# Input
user_speed = float(input("Enter your speed: "))
user_speed_limit = float(input("Enter the speed limit: "))

# Calculate the speed over the limit
speed_over_limit = user_speed - user_speed_limit

# TODO: Determine the fine based on the speed over the limit
# Use a single compound Boolean expression for efficiency
if 0 < speed_over_limit <= FINE_THRESHOLD_1:
    fine_amount = 309
elif FINE_THRESHOLD_1 < speed_over_limit <= FINE_THRESHOLD_2:
    fine_amount = 464
elif FINE_THRESHOLD_2 < speed_over_limit <= FINE_THRESHOLD_3:
    fine_amount = 696
elif FINE_THRESHOLD_3 < speed_over_limit <= FINE_THRESHOLD_4:
    fine_amount = 1161
elif speed_over_limit > FINE_THRESHOLD_4:
    fine_amount = 1780
else:
    fine_amount = 0

# Output the fine amount
print("Your fine is: $", fine_amount, sep="")

# ======================= end of Task 6. Speeding Fines ==============================================
