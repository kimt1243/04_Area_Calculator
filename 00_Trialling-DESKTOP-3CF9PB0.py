import random


# User input function - uses one function to get the users input for the difficulty and for the instructions
def valid_checker(question, search_list, error):
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


# number checker that checks if the user input is a valid
def input_checker(question, allow_floats="no"):
    while True:
        response = input(question)

        # returns continuous mode
        if response == '' and allow_floats == "no":
            return response

        elif response == 'xxx':
            return None
        elif response != "":
            try:
                response = float(response) if allow_floats == "yes" else int(response)
                if response < 1:
                    print("Please input a valid number greater than or equal to 1\n")
                else:
                    return response
            except ValueError:
                print("<Error> That is an invalid integer / number!\n")


# Question generator that is based on the difficulty the user chose.
def question_gen(diff_ask):
    # Available variables that will be used for the areas.
    height = random.randint(1, 10)
    width = random.randint(1, 10)
    base = random.randint(1, 10)
    radius = random.randint(1, 10)

    area = ''

    if diff_ask == "easy":
        area = height * width
        print(f"If the height of the square is {height} and the width is {width}, find the area.")
    elif diff_ask == "medium":
        area = 0.5 * base * height
        print(f"Imagine the area of a triangle if the base is {base} and the height is {height}.")
    elif diff_ask == "hard":
        area = 3.14 * radius ** 2
        print(f"Find the area of a circle if the radius is {radius}, (PI is set as 3.14).")

    user_answer = input_checker("Your answer: ", allow_floats="no")
    if user_answer is None:
        return "exit", None

    if user_answer == area:
        print("Correct! You calculated the area correctly!")
        return "correct", area
    else:
        print("Incorrect. The correct answer is", area)
        return "wrong", area


# Main Function
def main():
    yes_no_list_checker = {"yes", "no", "xxx"}
    difficulty_checker = {"easy", "medium", "hard", "xxx"}

    round_correct = 0
    round_wrong = 0

    print("====================================")
    print("Welcome to the Area Calculator Quiz!")
    print("====================================")
    print()

    # Ask if the player wants to see the instructions
    played_before = valid_checker("Would you like to see the instructions? ", yes_no_list_checker,
                                  "Please type either yes or no ('xxx' to exit)")
    if played_before == "yes":
        instructions()
    elif played_before == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        return "exit"

    # Ask if the player wants to see the formula list
    formula_check = valid_checker("Would you like to see the formula list? ", yes_no_list_checker,
                                  "Please type a either yes or no ('xxx' to exit)")
    if formula_check == "yes":
        display_formula_instructions()
    elif formula_check == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        return "exit"

    # Ask the player to choose the difficulty level
    diff_ask = valid_checker("Which difficulty would you like to play? ", difficulty_checker,
                             "Please type a valid difficulty (easy, medium, hard)")
    if diff_ask == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        return "exit"

    print("-----------------------------------")
    print(f"You have chosen the {diff_ask} difficulty!")
    print("------------------------------------")

    # Ask the player how many rounds they want to play
    rounds = input_checker('How many ROUNDS would you like to play? <enter> for continuous mode: ')
    if rounds is None:  # if user presses enter
        print('Thanks for playing! ')
        exit()
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


# Call the main() function and capture the returned values
game_stats = main()
stats_round_correct = 0
stats_round_wrong = 0

# Check if the return value is "exit" (when 'xxx' is typed during instructions or difficulty selection)
if game_stats == "exit":
    print("Thank you for playing!")
else:
    stats_round_correct, stats_round_wrong = game_stats

    # Calculate Game Stats
    stats_rounds_played = stats_round_correct + stats_round_wrong

    if stats_rounds_played == 0:
        percent_correct = 0.0
        percent_wrong = 0.0
    else:
        percent_correct = stats_round_correct / stats_rounds_played * 100
        percent_wrong = stats_round_wrong / stats_rounds_played * 100

    # Displays game stats with % values to the nearest whole number
    print("\n===== Game Statistics =====")
    print(f"QUESTIONS Played: {stats_rounds_played}")
    print(f"RIGHT!: {stats_round_correct}, ({percent_correct:.0f}%)")
    print(f"WRONG...: {stats_round_wrong}, ({percent_wrong:.0f}%)")