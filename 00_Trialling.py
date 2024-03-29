import random


# User input function - uses one function to get the users input for the difficulty and for the instructions
def yes_no_difficulty_checker(question, search_list, error):
    while True:
        response = input(question).lower()

        # Searches and checks the list (depending on the question) for valid responses, otherwise prints an error
        for item in search_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# Function that displays Instructions
def instructions():
    print()
    print("===========================================================================================")
    print("                                       INSTRUCTIONS                                        ")
    print("===========================================================================================")
    print()
    print("                            For each quiz, you will be asked to:                           ")
    print()
    print("                        Choose a difficulty for your math question.                        ")
    print("                                Easy mode contains squares.                                ")
    print("                              Medium mode contains triangles.                              ")
    print("                                Hard mode contains circles.                                ")
    print()
    print("  Enter the number of questions (or press enter for infinite rounds) that you want to play.")
    print()
    print("===========================================================================================")
    print("                             Can you guess the correct area?                               ")
    print("===========================================================================================")
    print()


# Function that displays formula instructions
def display_formula_instructions():
    print()
    print("===============================================================================")
    print("                                     FORMULA                                   ")
    print("===============================================================================")
    print()
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|    The formula for finding the area of a SQUARE is: area = height * width   |")
    print("|-----------------------------------------------------------------------------|")
    print("|The formula for finding the area of a TRIANGLE is: area = 0.5 * base * height|")
    print("|-----------------------------------------------------------------------------|")
    print("|   The formula for finding the area of a CIRCLE is: area = PI * radius^2     |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print()
    print("===============================================================================")
    print("                       PI is set as *3.14* in this game                        ")
    print("===============================================================================")
    print()


# Round checker that makes sure the user enters a valid number of rounds

# Input checker function
def input_checker(question, is_integer=False, allow_empty=True, min_value=None):
    while True:
        response = input(question)
        if response == "" and not allow_empty:
            print("Please enter a value.")
            continue
        if is_integer:
            try:
                response = int(response)
            except ValueError:
                print("Please enter a valid integer.")
                continue
        else:
            try:
                response = float(response)
            except ValueError:
                print("Please enter a valid number.")
                continue

        if min_value is not None and response < min_value:
            print(f"Please enter a number greater than or equal to {min_value}.")
            continue

        return response

# Round checker that makes sure the user enters a valid number of rounds
def round_checker():
    return input_checker("How many QUESTIONS would you like to play? (press enter for Continuous mode): ",
                         is_integer=True, allow_empty=True, min_value=1)

# int/float checker, used for components consisting of checking integers
def intfloat_checker(question, exit_code=None, allow_floats=True):
    return input_checker(question, is_integer=not allow_floats, allow_empty=exit_code is None, min_value=1)


# Question generator that is based on the difficulty the user chose.
def question_gen(diff_ask):
    # Available variables that will be used for the areas.
    height = random.randint(1, 10)
    width = random.randint(1, 10)
    base = random.randint(1, 10)
    radius = random.randint(1, 10)

    if diff_ask == "easy":
        area = height * width
        print(f"If the height of the square is {height} and the width is {width}, find the area.")
    elif diff_ask == "medium":
        area = 0.5 * base * height
        print(f"Imagine the area of a triangle if the base is {base} and the height is {height}.")
    elif diff_ask == "hard":
        area = 3.14 * radius ** 2
        print(f"Find the area of a circle if the radius is {radius}, (PI is set as 3.14).")

    user_answer = intfloat_checker("Your answer: ", exit_code="xxx", allow_floats="no")
    if user_answer is None:
        return "exit", None

    if user_answer == area:
        print("Correct! You calculated the area correctly!.")
        return "correct", area
    else:
        print("Incorrect. The correct answer is", area)
        return "wrong", area


# Main Function
# Available lists
yes_no_checker = {"yes", "no", "xxx"}
difficulty_checker = {"easy", "medium", "hard", "xxx"}


def play_game():
    round_correct = 0
    round_wrong = 0

    print("====================================")
    print("Welcome to the Area Calculator Quiz!")
    print("====================================")
    print()

    # Ask if the player wants to see the instructions
    played_before = yes_no_difficulty_checker("Would you like to see the instructions? ", yes_no_checker,
                                              "Please enter either yes or no (or 'xxx' to exit)")
    if played_before == "yes":
        instructions()
    elif played_before == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        return "exit"

    # Ask if the player wants to see the formula list
    formula_check = yes_no_checker("Would you like to see the formula list? ")
    if formula_check == "yes":
        display_formula_instructions()
    elif formula_check == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        return "exit"

    # Ask the player to choose the difficulty level
    diff_ask = yes_no_difficulty_checker("Which difficulty would you like to play? ", difficulty_checker,
                                         "Please enter a valid difficulty (easy, medium, hard")
    if diff_ask == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        return "exit"

    print("-----------------------------------")
    print(f"You have chosen the {diff_ask} difficulty!")
    print("------------------------------------")

    # Ask the player how many rounds they want to play
    rounds = round_checker()
    rounds_played = 0

    while True:
        print()
        if rounds == "":
            heading = f"Continuous Mode: QUESTION {rounds_played + 1}"
        else:
            heading = f"!QUESTION {rounds_played + 1} of {rounds}!"
        print(heading)

        result, area = question_gen(diff_ask)

        # End game if exit code is typed
        if result == "exit" and rounds_played > 0:
            print("\nYou have chosen to exit the Quiz. Thank you for playing!\n")
            break
        elif result == "exit":
            print("You have to play at least one QUESTION!")
            continue

        if result == "correct":
            round_correct += 1
        else:
            round_wrong += 1

        rounds_played += 1

        if rounds_played == rounds:
            break

    return round_correct, round_wrong


# Call the play_game() function and capture the returned values
game_stats = play_game()

# Check if the return value is "exit" (when 'xxx' is typed during instructions or difficulty selection)
if game_stats == "exit":
    print("Thank you for playing!")
else:
    round_correct, round_wrong = game_stats

    # Calculate Game Stats
    rounds_played = round_correct + round_wrong
    percent_correct = round_correct / rounds_played * 100
    percent_wrong = round_wrong / rounds_played * 100

    # Displays game stats with % values to the nearest whole number
    print("\n===== Game Statistics =====")
    print(f"QUESTIONS Played: {rounds_played}")
    print(f"RIGHT!: {round_correct}, ({percent_correct:.0f}%)")
    print(f"WRONG...: {round_wrong}, ({percent_wrong:.0f}%)")
