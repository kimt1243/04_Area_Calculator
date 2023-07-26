import random
yesno_list = ["yes", "no", "xxx"]
questiondiff_list = ["easy", "medium", "hard", "xxx"]


# Function that checks if the response is in the yesno_list
def yes_no_checker(question):
    while True:
        response = input(question).lower()
        for item in yesno_list:
            if response == item[0] or response == item:
                return item
        else:
            print("Please type either yes or no")


# Displays Instructions
def instructions():
    print()
    print("***********************")
    print("**** INSTRUCTIONS *****")
    print("***********************")
    print()
    print("For each QUESTION, you will be asked to:")
    print()
    print("+ Choose a difficulty for your math question.")
    print("  = Easy mode contains square/rectangles.")
    print("  = Medium mode contains triangles.")
    print("  = Hard mode contains circles.")
    print()
    print("- Enter the number of questions (or press enter for infinite rounds) that you want to play.")
    print("*Can you guess the correct area?*")
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


# Question checker that makes sure the user enters a valid round
def question_checker():
    while True:
        response = input("How many QUESTIONS would you like to play (press enter for infinite Question): ")
        response_error = "Please type either <enter> or an integer that is a whole number and more than 0"
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

                elif allow_floats == "no":
                    response = int(response)

                if response < 1:
                    print("Please input a valid Number over '1' \n")
                    continue

            except ValueError:
                print("<Error> That is an invalid Integer / Number!\n")
                continue

        return response


# Question generator that is based on the difficulty the user chose.
def question_gen(diff_ask):
    while diff_ask not in questiondiff_list:
        print("Invalid difficulty level. Please choose from: easy, medium, or hard.")
        diff_ask = input("Enter the difficulty: ").lower()

    if diff_ask == "easy":
        height = random.randint(1, 10)
        width = random.randint(1, 10)
        area = height * width
        print("If the height of the square/rectangle is {} and the width is {}, find the area.".format(height, width))

    elif diff_ask == "medium":
        height = random.randint(1, 10)
        base = random.randint(1, 10)
        area = 0.5 * base * height
        print("Find the area of a triangle if the base is {} and the height is {}.".format(base, height))

    elif diff_ask == "hard":
        radius = random.randint(1, 10)
        area = 3.14 * radius ** 2
        print("Find the area of a circle if the radius is {}, (PI is set as 3.14).".format(radius))

    user_answer = float(input("Your answer: (Enter xxx to exit) "))
    if user_answer == area:
        print("Correct! You calculated the area correctly.")
        return "right"
    else:
        print("Incorrect. The correct answer is", area)
        return "wrong"


# Main Function
def play_game():

    question_right = 0
    question_wrong = 0

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
        print("================================")
        print("PI is set as *3.14* in this game")
        print("================================")
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
    question = question_gen(diff_ask)
    question_played = 0
    while True:
        print()
        if question == "":
            heading = "Continuous Mode: Question {}".format(question_played + 1)
        else:
            heading = "!Question {} of {}!".format(question_played + 1, question)
        print(heading)
        result = question_gen(diff_ask)
        if result == "exit":
            print()
            print("#You have chosen 'xxx'. Thank you for playing!#")
            break
        if result == "right":
            question_right += 1
        else:
            question_wrong += 1
        question_played += 1
        if question_played == question:
            break

    return question_right, question_wrong


# Call the play_game() function and capture the returned values
question_right, question_wrong = play_game()

# Calculate Game Stats
question_played = question_right + question_wrong
percent_right = question_right / question_played * 100
percent_wrong = question_wrong / question_played * 100

print()

# Displays game stats with % values to the nearest whole number
print("===== Game Statistics =====")
print("Questions Played: {}".format(question_played))
print(f"Right: {question_right}, ({percent_right:.0f}%) \nLose: {question_wrong}, ({percent_wrong:.0f}%)")
