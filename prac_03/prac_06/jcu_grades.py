# 3. JCU Grades
import random


def main():
    """Display JCU grades from user scores and random ones."""
    score = float(input("Enter score: "))
    while score >= 0:
        grade = determine_grade(score)
        print(f"The score {score} is {grade}")
        score = float(input("Enter score: "))

    number_of_scores = int(input("How many random scores: "))
    for i in range(number_of_scores):
        score = random.randint(0, 99)  # Adjusted to exclude 100
        grade = determine_grade(score)
        print(f"{score} = {grade}")


def determine_grade(score):
    """Determine JCU grade based on the given score."""
    if score < 50:
        return "F"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    return "HD"


main()
