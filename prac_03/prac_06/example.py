"""
CP1401 - Example program for Practical 6 - Functions
BMI calculation example
"""


# def main():
#     # height = float(input("Height (m): "))
#     # weight = float(input("Weight (kg): "))
#     height = get_valid_number("Height (m): ", 0, 3)
#     weight = get_valid_number("Weight (kg): ", 0, 300)
#     bmi = calculate_bmi(height, weight)
#     category = determine_weight_category(bmi)
#     print(f"This BMI is {bmi}, which is considered {category}")
#
#
# def get_valid_number(prompt, low, high):
#     number = float(input(prompt))
#     while number < low or number > high:
#         print("Invalid input")
#         number = float(input(prompt))
#     return number
#
#
# def calculate_bmi(height, weight):
#     return weight / (height ** 2)
#
#
# def determine_weight_category(bmi):
#     # Note that we don't use the if, elif, else pattern here
#     # because we return, making "elif" and "else" redundant
#     if bmi < 18.5:
#         return "underweight"
#     if bmi < 25:
#         return "normal"
#     if bmi < 30:
#         return "overweight"
#     return "obese"
#
#
# def run_tests():
#     bmi = calculate_bmi(2, 60)
#     print(bmi)  # This should be 15.0
#     bmi = calculate_bmi(1.5, 100)
#     print(bmi)  # This should be 44.4
#
#     print(determine_weight_category(16))  # This should be underweight
#     print(determine_weight_category(25))  # This should be overweight
#
#     height = get_valid_number("Height (m): ", 0, 3)
#     print(height)
#     weight = get_valid_number("Weight (kg): ", 0, 300)
#     print(weight)
#
#
# main()
# run_tests()

# ============================== things to do =====================================
def main():
    height = get_valid_number("Height (m): ", 0, 3)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    age = get_valid_number("Age: ", 0, 150)  # Adjust the age range as needed
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi:.1f}, which is considered {category}. Age: {age}")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"


def run_tests():
    # Test cases for each weight category
    print(determine_weight_category(16))  # This should be underweight
    print(determine_weight_category(22))  # This should be normal
    print(determine_weight_category(28))  # This should be overweight
    print(determine_weight_category(32))  # This should be obese

    # Additional test cases for calculate_bmi
    bmi = calculate_bmi(2, 60)
    print(bmi)  # This should be 15.0
    bmi = calculate_bmi(1.5, 100)
    print(bmi)  # This should be 44.4


# Uncomment the lines below to run the main function and tests
main()
run_tests()


