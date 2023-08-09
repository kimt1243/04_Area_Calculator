import random


# Displays Instructions
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


# Displays formula instructions
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


# User input function - uses one function to get the users input for the difficulty and for the instructions
def valid_checker(question, search_list, error):
    while True:
        response = input(question).lower()

        # Searches and checks the list (depending on the question) for valid responses, otherwise prints an error
        for item in search_list:
            if response == item[0] or response == item:
                return item

        # Prints error code if the user answer is not a valid answer.
        print(error)
        print()


# int/float checker, used for components consisting of checking integers
def input_checker(question, allow_floats=False):
    while True:
        response = input(question)

        # returns continuous mode.
        if response == '' and allow_floats is False:
            return response

        # returns the exit code when user enters 'xxx'
        elif response == 'xxx':
            return 'xxx'

        elif response != "":
            try:
                if allow_floats is True:
                    response = float(response)

                elif allow_floats is False:
                    response = int(response)

                # if response is lower than 1, print number error.
                if response < 1:
                    print()
                    print("Please input a valid number greater than or equal to 1\n")
                else:
                    return response
            # if user answer is not an integer / number, print ValueError
            except ValueError:
                print()
                print("<Error> That is an invalid integer / number!\n")


# Question generator that is based on the difficulty the user chose.
def question_gen(difficulty):

    # Available variables that will be used for the areas.
    height = random.randint(1, 10)
    width = random.randint(1, 10)
    base = random.randint(1, 10)
    radius = random.randint(1, 10)

    question = ''

    area = ''

    # If the difficulty is "easy", output a square/rectangle question.
    if difficulty == "easy":
        area = height * width
        question = f"If the height of the square/rectangle is {height} and the width is {width}, find the area: "

    # If the difficulty is "medium", output a triangle question.
    elif difficulty == "medium":
        area = 0.5 * base * height
        question = f"Imagine the area of a triangle if the base is {base} and the height is {height}: "

    # If the difficulty is "hard", output a circle question.
    elif difficulty == "hard":
        area = 3.14 * radius ** 2
        question = f"Find the area of a circle if the radius is {radius}, (PI is set as 3.14): "

    # returns the area and question.
    return area, question


# Main Function
def main():

    # Available Lists
    yes_no_list_checker = {"yes", "no", "xxx"}
    difficulty_checker = {"easy", "medium", "hard", "xxx"}

    # Available variables
    questions_played = 0
    question_correct = 0
    question_wrong = 0
    user_answer = ''

    print("====================================")
    print("Welcome to the Area Calculator Quiz!")
    print("====================================")
    print()

    # Ask if the player wants to see the instructions.
    played_before = valid_checker("Would you like to see the instructions? ", yes_no_list_checker,
                                  "Please type either yes or no ('xxx' to exit)")
    print()
    # if user enters 'yes', print instructions.
    if played_before == "yes":
        instructions()

    # if the user answer is 'xxx' when they are asked if they want to see the instructions, exit the code.
    elif played_before == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        exit()

    # Ask if the player wants to see the formula list.
    formula_check = valid_checker("Would you like to see the formula list? ", yes_no_list_checker,
                                  "Please type a either yes or no ('xxx' to exit)")
    print()

    # if user enters 'yes', print formula.
    if formula_check == "yes":
        display_formula_instructions()

    # if the user answer is 'xxx' when they are asked if they want to see the formula, exit the code.
    elif formula_check == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        exit()

    # Ask the player to choose the difficulty level
    user_difficulty = valid_checker("Which difficulty would you like to play? ", difficulty_checker,
                                    "Please type a valid difficulty (easy, medium, hard)")
    print()

    # if the user answer is 'xxx' when they are asked to enter the difficulty of the question
    # they want to play, exit the code.
    if user_difficulty == "xxx":
        print("You have chosen 'xxx'. Thank you for playing!")
        exit()

    # prints which difficulty the user has chosen.
    print("-----------------------------------")
    print(f"You have chosen the {user_difficulty} difficulty!")
    print("------------------------------------")
    print()

    # Ask the player how many questions they want to play
    questions = input_checker('How many QUESTIONS would you like to play? <enter> for continuous mode: ')

    # if the user answer is 'xxx' when they are asked to enter the amount of question they want to play, exit the code.
    if questions == 'xxx':
        print("You have chosen 'xxx'. Thank you for playing!")
        exit()

    while True:
        print()
        # if the user chooses <enter> for number of questions, print Continuous questions.
        if questions == "":
            heading = f"Continuous Mode: QUESTION {questions_played + 1}"

        # if the user chooses a valid number for number of questions, print Questions.
        else:
            heading = f"!QUESTION {questions_played + 1} of {questions}!"
        print(heading)

        area, math_question = question_gen(user_difficulty)

        # checks the type of value of answer, sets input_checker accordingly.
        if isinstance(area, float):
            user_answer = input_checker(math_question, True)
        elif isinstance(area, int):
            user_answer = input_checker(math_question, False)

        # if the users answer is 'xxx' but the user has not played more than 1 question, make the user play one question
        if user_answer == "xxx" and questions_played == 0:
            print("You have to play at least one QUESTION!")
            continue

        # If the user answer is 'xxx' and they have played more than one question, exit game.
        elif user_answer == "xxx":
            print("\nYou have chosen to exit the Quiz. Thank you for playing!\n")
            break

        # If the user answer is the same as the area, + 1 to the question correct value.
        if user_answer == area:
            print("Correct! You calculated the area correctly!")
            question_correct += 1

        # If the user answer is not the same as the area, + 1 to the question wrong value.
        else:
            print("Incorrect. The correct answer is", area)
            question_wrong += 1

        questions_played += 1

        # If the amount of questions played is the same as the amount of questions
        # that the user wanted to play at the start, break game.
        if questions_played == questions:
            break

    return question_correct, question_wrong


# Call the main() function and capture the returned values
game_stats = main()
stats_question_correct = 0
stats_question_wrong = 0

# Check if the return value is "exit" (when 'xxx' is typed during instructions or difficulty selection)
if game_stats == "exit":
    print("Thank you for playing!")
else:
    stats_question_correct, stats_question_wrong = game_stats

    # Calculate Game Stats.
    stats_question_played = stats_question_correct + stats_question_wrong

    # Calculate percentage stats.
    percent_correct = stats_question_correct / stats_question_played * 100
    percent_wrong = stats_question_wrong / stats_question_played * 100

    # Displays game stats with % values to the nearest whole number
    print("\n===== Game Statistics =====")
    print(f"QUESTIONS Played: {stats_question_played}")
    print(f"RIGHT!: {stats_question_correct}, ({percent_correct:.0f}%)")
    print(f"WRONG...: {stats_question_wrong}, ({percent_wrong:.0f}%)")