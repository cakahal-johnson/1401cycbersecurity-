# 1. Error Checking
while True:
    try:
        # Get user input for worker level
        worker_level = int(input("Worker level: "))

        # Check if worker level is within the valid range (1 to 10 inclusive)
        if 1 <= worker_level <= 10:
            # Calculate and print the salary
            salary = worker_level * 5000
            print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")
            break  # Exit the loop if the input is valid
        else:
            print("Invalid worker level. Please enter a value between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Example test data:
# Worker level: 0 (Invalid input)
# Worker level: 11 (Invalid input)
# Worker level: 7 (Valid input)

# 2. Number Sequences

# a. Displaying odd numbers between 1 and 100:

# Loop to display odd numbers between 1 and 100
for number in range(1, 101, 2):
    print(number)

# b. Displaying Summer Olympic years between 1896 and today:

# Loop to display Summer Olympic years between 1896 and today (every 4 years)
current_year = 2024
for year in range(1896, current_year + 1, 4):
    print(year, end=" ")

# c. Displaying a sequence (e.g., multiples of 3):

# Loop to display multiples of 3 up to 30
# Chosen sequence: Multiples of 3
for multiple in range(3, 31, 3):
    print(multiple)

# 3. Write a program that prints smiley and frowny faces until the user quits.

print("Hey there! please select as follows: (S)miley (F)rowny (Q)uit")
choice = input("> ").upper()
while choice != "Q":
    if choice == "S":
        print(":)")
    elif choice == "F":
        print(":(")
    else:
        print("Invalid choice")
    print("(S)miley (F)rowny (Q)uit")
    choice = input("> ").upper()
print("Farewell")

# 4. Average Age
total_age = 0
number_of_people = 0
age = int(input("Age: "))
while age >= 0:
    total_age += age
    number_of_people += 1
    age = int(input("Age: "))
if number_of_people != 0:
    average = total_age / number_of_people
    print(average)
else:
    print("No valid average")

# 5. Guessing Game
SECRET = 6
guess_count = 0

while True:
    guess = int(input("Guess a number: "))
    guess_count += 1  # Increment the guess count

    if guess < SECRET:
        print("Higher")
    elif guess > SECRET:
        print("Lower")
    else:
        print(f"You got it in {guess_count} {'guess' if guess_count == 1 else 'guesses'}!")
        break

# 6. Nested Loops
number_of_rows = int(input("Rows: "))
number_of_columns = int(input("Columns: "))
for i in range(number_of_rows):
    for j in range(number_of_columns):
        print(j, end=" ")
    print()
