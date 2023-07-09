import random
import math

# List goes here
Formula_list = ["square", "triangle", "circle", "xxx"]
yesno_list = ["yes", "no", "xxx"]
questiondiff_list = ["easy", "medium", "hard", "xxx"]


def yes_no_checker(question):
    while True:
        # Ask user for choice
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item),
        # the full item is returned

        for item in yesno_list:
            if response == item[0] or response == item:
                return item
        else:
            print("Please type either yes or no")


def instructions():
    print()
    print("***********************")
    print("**** INSTRUCTIONS *****")
    print("***********************")
    print()
    print("For each game, you will be asked to:")
    print()
    print("- Choose a difficulty for your math question.")
    print("  - Easy mode contains squares. ")
    print("  - Medium mode contains triangles. ")
    print("  - Hard mode contains circles. ")
    print()
    print("- Enter the number of rounds (or press enter for infinite rounds) that you want to play.")
    print("- Can you guess the correct area?")
    print()
    return ""


def formula_checker(question):
    while True:
        # Ask user for choice
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item),
        # the full item is returned

        for item in Formula_list:
            if response == item[0] or response == item:
                return item

        else:
            print()
            print("Please type a valid formula (square, triangle, circle)")
            print()


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
            print("Please type a valid difficulty (easy, medium, hard)")
            print()


def round_checker():
    while True:
        response = input("How many rounds would you like to play (press enter for infinite rounds): ")

        response_error = ("Please type either <enter> or an integer "
                          "that is a whole number and more than 0")

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(response_error)
                    continue

            except ValueError:
                print(response_error)
                continue

        return response


def int_check(question, exit_code=None, previous_guesses=None):
    while True:
        response = input(question).lower()

        if response == exit_code:
            return None

        if response == "xxx":
            return response

        try:
            number = int(response)

            if previous_guesses is not None and number in previous_guesses:
                print("You have already guessed that number. Please try a different one.")
                continue

            return number

        except ValueError:
            print("Invalid input. Please enter an integer.")


def question_gen(diff_ask, previous_guesses):
    if diff_ask == "easy":
        height = random.randint(1, 10)
        width = random.randint(1, 10)
        area = height * width
        print("If the height of the square is {} and the width is {}, find the area.".format(height, width))
        user_answer = int_check("Your answer: ", exit_code="xxx", previous_guesses=previous_guesses)

        if user_answer is None:
            return "exit"

        if user_answer == area:
            print("Correct! You calculated the area correctly.")
            return "win"
        else:
            print("Incorrect. The correct answer is", area)
            return "lose"

    elif diff_ask == "medium":
        base = random.randint(1, 10)
        height = random.randint(1, 10)
        area = 0.5 * base * height
        print("Find the area of a triangle if the base is {} and the height is {}.".format(base, height))
        user_answer = int_check("Your answer: ", exit_code="xxx", previous_guesses=previous_guesses)

        if user_answer is None:
            return "exit"

        if user_answer == area:
            print("Correct! You calculated the area correctly.")
            return "win"
        else:
            print("Incorrect. The correct answer is", area)
            return "lose"

    elif diff_ask == "hard":
        radius = random.randint(1, 10)
        area = math.pi * radius ** 2
        print("Find the area of a circle if the radius is {}.".format(radius))
        user_answer = int_check("Your answer: ", exit_code="xxx", previous_guesses=previous_guesses)

        if user_answer is None:
            return "exit"

        if user_answer == area:
            print("Correct! You calculated the area correctly.")
            return "win"
        else:
            print("Incorrect. The correct answer is", area)
            return "lose"


# Main routine goes here
def play_game():
    print("====================================")
    print("Welcome to the Area Calculator Game!")
    print("====================================")
    print()

    played_before = yes_no_checker("Would you like to see the instructions? ")
    print()

    if played_before == "yes":
        instructions()

    if played_before == "xxx":
        print()
        print("You have chosen 'xxx'. Thank you for playing!")
        return

    formula_check = yes_no_checker("Would you like to see the formula list? ")
    print()

    if formula_check == "yes":
        print("The formula for finding the area of a SQUARE is: area = height * width")
        print("The formula for finding the area of a TRIANGLE is: area = 0.5 * base * height")
        print("The formula for finding the area of a CIRCLE is: area = PI * radius^2")
        print()

    if formula_check == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        return

    diff_ask = difficulty_checker("Which difficulty would you like to play? ")

    if diff_ask == "xxx":
        print()
        print("You have chosen 'xxx'. Thank you for playing!")
        return "exit"

    print("------------------------------------")
    print("You have chosen the {} difficulty!".format(diff_ask))
    print("------------------------------------")

    rounds_played = 0

    # Ask user for # of rounds, <enter> for infinite mode
    rounds = round_checker()

    if rounds == "xxx":
        print()
        print("You have chosen 'xxx'. Thank you for playing!")
        return

    game_summary = {"win": 0, "lose": 0}

    while True:
        # Rounds Heading
        print()
        if rounds == "":
            heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        else:
            heading = "Round {} of {}".format(rounds_played + 1, rounds)

        print(heading)

        previous_guesses = []

        result = question_gen(diff_ask, previous_guesses)

        if result == "exit":
            print()
            print("You have chosen 'xxx'. Thank you for playing!")
            break

        if result == "win":
            game_summary["win"] += 1
        else:
            game_summary["lose"] += 1

        rounds_played += 1

        # End game if number of rounds < number of rounds played
        if rounds_played == rounds:
            break

    print()
    print("***** Game Summary *****")
    print("Total Rounds Played:", rounds_played)
    print("Wins:", game_summary["win"])
    print("Losses:", game_summary["lose"])
    print()

    print("Thank you for playing the Area Calculator Game!")
    print()


play_game()
