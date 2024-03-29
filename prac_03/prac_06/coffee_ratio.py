# 1. Coffee Brew Ratio
def main():
    """Get user's coffee details and display what kind of brew it is."""
    dose = get_valid_number("Enter the amount of ground coffee (Dose in grams): ", 0, 100)
    coffee_yield = get_valid_number("Enter the amount of brewed coffee (Yield in grams): ", 0, 200)
    ratio = coffee_yield / dose
    style = determine_coffee_style(ratio)
    print(f"1:{ratio:.1f} is considered {style}")


def determine_coffee_style(ratio):
    """Determine the style of coffee based on the brew ratio."""
    if ratio < 2:
        return "ristretto"
    elif ratio < 3:
        return "normale"
    else:
        return "lungo"


def get_valid_number(prompt, low, high):
    """Get a valid number between low and high inclusive."""
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def check_coffee():
    """Run quick tests to ensure determine_coffee_style works as expected."""
    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(3.5)
    print(style)  # This should be lungo


def check_coffee_loop():
    """Run through a number of brew ratios, printing the style for each."""
    for i in range(0, 5):
        ratio = i + 0.5
        style = determine_coffee_style(ratio)
        print(f"1:{ratio} is considered {style}")


# check_coffee()
# check_coffee_loop()
main()


# ============================== coffee ================================
