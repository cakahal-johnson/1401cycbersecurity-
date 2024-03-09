# 2. Parity
def print_parity(number):
    parity = number % 2
    print(f"Parity of {number} should be {parity}: {parity}")


def get_parity(number):
    return number % 2


def is_odd(number):
    return number % 2 == 1


def main():
    # Part 1: Test print_parity function
    print_parity(4)  # Expected: Parity of 4 should be 0: 0
    print_parity(41)  # Expected: Parity of 41 should be 1: 1

    # Part 2: Test get_parity function
    parity_4 = get_parity(4)
    parity_41 = get_parity(41)
    print(f"Parity of 4 should be 0: {parity_4}")
    print(f"Parity of 41 should be 1: {parity_41}")

    # Part 3: Test is_odd function
    odd_result = is_odd(7)
    even_result = is_odd(10)
    print(f"Is 7 odd? {odd_result}")  # Expected: True
    print(f"Is 10 odd? {even_result}")  # Expected: False

    # Additional test for is_odd function
    age = int(input("Age: "))
    if is_odd(age):
        print("Name in capitals")
    else:
        print("Name in lowercase")

# Run the main function
main()
