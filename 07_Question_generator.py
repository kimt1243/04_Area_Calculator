import math
import random

questiondiff_list = ["easy", "medium", "hard"]


def difficulty_checker(question):
    while True:
        # Ask user for choice
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item),
        # the full item is returned
        for item in questiondiff_list:
            if response == item[0] or response == item:
                return item
        else:
            print()
            print("Please type either easy, medium, or hard.")
            print()


def int_check(question, exit_code=None):
    while True:
        response = input(question).lower()

        if response == exit_code:
            break

        try:
            return int(response)

        except ValueError:
            print("Invalid input. Please enter an integer.")


# Main Routine goes here...
diff_ask = difficulty_checker("Which difficulty would you like to play? ")


def Question_gen():
    if diff_ask == "easy":
        height = random.randint(1, 10)
        width = random.randint(1, 10)
        area = height * width
        print("If the height of the square is {} and the width is {}, find the area.".format(height, width))
        user_answer = int_check("Your answer: ")
        if user_answer == area:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", area)

    if diff_ask == "medium":
        base = random.randint(1, 10)
        height = random.randint(1, 10)
        area = 0.5 * base * height
        print("Find the area of a triangle if the base is {} and the height is {}.".format(base, height))
        user_answer = int_check("Your answer: ")
        if user_answer == area:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", area)

    if diff_ask == "hard":
        radius = random.randint(1, 10)
        area = math.pi * radius ** 2
        print("Find the area of a circle if the radius is {}.".format(radius))
        user_answer = int_check("Your answer: ")
        if user_answer == area:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", area)


Question_gen()