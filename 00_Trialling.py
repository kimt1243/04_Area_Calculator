import random

yesno_list = ["yes", "no", "xxx"]
questiondiff_list = ["easy", "medium", "hard", "xxx"]


def yes_no_checker(question):
    while True:
        response = input(question).lower()
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
    print("  - Easy mode contains squares.")
    print("  - Medium mode contains triangles.")
    print("  - Hard mode contains circles.")
    print()
    print("- Enter the number of rounds (or press enter for infinite rounds) that you want to play.")
    print("- Can you guess the correct area?")
    print()

# Function that checks that the difficulty the user entered is a valid difficulty.
def difficulty_checker(question):
    while True:
        response = input(question).lower()
        for item in questiondiff_list:
            if response == item[0] or response == item:
                return item
        else:
            print()
            print("Please type a valid difficulty (easy, medium, hard)")
            print()

# Round checker that makes sure the user
def round_checker():
    while True:
        response = input("How many rounds would you like to play (press enter for infinite rounds): ")
        response_error = ("Please type either <enter> or an integer that is a whole number and more than 0")
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


# int/float checker, used for components consisting of checking integers
def intfloat_checker(question, exit_code=None, allow_floats="yes"):

    while True:
        response = input(question)

        if response == exit_code:
            return None

        elif response != "":
            try:
                if allow_floats == "yes":
                    response = float(response)

                    # When implemented into base, no sides (which the user has to find) will be less than 1
                    if response < 1:
                        print("Please input a valid NUMBER (> 1)\n")
                        continue

                elif allow_floats == "no":
                    response = int(response)

                    if response < 1:
                        print("Please input a valid integer (> 0)\n")
                        continue

            except ValueError:
                print("<ValueError> That is an invalid INTEGER / NUMBER\n")
                continue

        return response

# Question generator that is based on the difficulty the user chose.
def question_gen(diff_ask):
    if diff_ask == "easy":
        height = random.randint(1, 10)
        width = random.randint(1, 10)
        area = height * width
        print("If the height of the square is {} and the width is {}, find the area.".format(height, width))
        user_answer = intfloat_checker("Your answer: ", exit_code="xxx", allow_floats="no")
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
        user_answer = intfloat_checker("Your answer: ", exit_code="xxx", allow_floats="no")
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
        area = 3.14 * radius ** 2
        print("Find the area of a circle if the radius is {}, (PI is set as 3.14).".format(radius))
        user_answer = intfloat_checker("Your answer: ", exit_code="xxx", allow_floats="yes")
        if user_answer is None:
            return "exit"
        if user_answer == area:
            print("Correct! You calculated the area correctly.")
            return "win"
        else:
            print("Incorrect. The correct answer is", area)
            return "lose"

# Main Function
def play_game():
    round_win = 0
    round_lose = 0

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
        print("PI is set as *3.14* in this game")
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
    rounds = round_checker()
    rounds_played = 0
    while True:
        print()
        if rounds == "":
            heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        else:
            heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)
        result = question_gen(diff_ask)
        if result == "exit":
            print()
            print("You have chosen 'xxx'. Thank you for playing!")
            break
        if result == "win":
            round_win += 1
        else:
            round_lose += 1
        rounds_played += 1
        if rounds_played == rounds:
            break

    return round_win, round_lose

# Call the play_game() function and capture the returned values
round_win, round_lose = play_game()

# Calculate Game Stats
rounds_played = round_win + round_lose
percent_win = round_win / rounds_played * 100
percent_lose = round_lose / rounds_played * 100

print()

# Displays game stats with % values to the nearest whole number
print("===== Game Statistics =====")
print("Rounds Played: {}".format(rounds_played))
print("Win: {}, ({:.0f}%) \nLose: {}, ({:.0f}%)".format(round_win, percent_win, round_lose, percent_lose))
