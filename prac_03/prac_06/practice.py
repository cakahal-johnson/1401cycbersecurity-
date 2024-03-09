import random


# A. Coffee Ratio Calculation
def calculate_brew_ratio(dose, yield_):
    """Calculate coffee brew ratio."""
    return yield_ / dose


def test_calculate_brew_ratio():
    """Test calculate_brew_ratio function."""
    assert calculate_brew_ratio(20, 40) == 2.0
    assert calculate_brew_ratio(18, 36) == 2.0
    assert calculate_brew_ratio(15, 45) == 3.0


def main_coffee_ratio():
    """Main program for coffee brew ratio calculation."""
    dose = float(input("Enter the dose (grams): "))
    yield_ = float(input("Enter the yield (grams): "))

    ratio = calculate_brew_ratio(dose, yield_)
    print(f"The brew ratio is: {ratio}")

# Uncomment the lines below to run the coffee ratio program
# test_calculate_brew_ratio()
main_coffee_ratio()


# B. Random Coffee:

def random_coffee_program():
    """Generate random coffee yield program."""
    dose = float(input("Enter the dose (grams): "))
    min_yield = 25  # Set your realistic minimum yield
    max_yield = 40  # Set your realistic maximum yield

    yield_ = random.uniform(min_yield, max_yield)
    print(f"The random yield is: {yield_}")

# Run the random coffee program
random_coffee_program()


# C. Reverse Words
def print_reversed_words(word1, word2):
    """Print two words in reverse order."""
    reversed_string = f"{word2} {word1}"
    print(reversed_string)

# Test the print_reversed_words function
print_reversed_words("hi", "ho")
