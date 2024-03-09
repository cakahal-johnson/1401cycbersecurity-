# 4. Add Functions to Previous Pracs
# Calculate salary for worker level


def get_valid_birth_month():
    """Get a valid birth month from the user."""
    birth_month = int(input("Enter your birth month: "))
    while not (1 <= birth_month <= 12):
        print("Invalid month")
        birth_month = int(input("Enter your birth month: "))
    return birth_month


def print_numbers_up_to_birth_month(birth_month):
    """Print numbers from 1 to the given birth month."""
    for count in range(1, birth_month + 1):
        print(count, end=" ")
    print()


def main():
    """Main program to get the birth month and print numbers up to it."""
    birth_month = get_valid_birth_month()

    if 1 <= birth_month <= 12:
        print_numbers_up_to_birth_month(birth_month)


# Run the main program
main()


# Print grid(rows, columns)
def print_round_names(round_number):
    """Print names for a given round."""
    for name in ["Miles", "Ella", "Chet"]:
        print("Round", round_number, "-", name)


def print_separator():
    """Print a separator line."""
    print("---------------------")


def main():
    """Main program to print round names and separators."""
    for round_number in range(1, 4):
        print_round_names(round_number)
        if round_number < 3:
            print_separator()


# Run the main program
main()

