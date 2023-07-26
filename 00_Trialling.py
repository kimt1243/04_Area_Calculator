import random

yesno_list = ["yes", "no", "xxx"]
questiondiff_list = ["easy", "medium", "hard", "xxx"]

# Function that checks user response against a list of valid options
def user_response_checker(question, valid_options, allow_exit=True):
    while True:
        response = input(question).lower()
        if response in valid_options:
            return response
        elif allow_exit and response == "xxx":
            print("\nYou have chosen 'xxx'. Thank you for playing!")
            return "exit"
        else:
            print("Invalid input. Please try again.")


# Function that generates the question based on difficulty
def question_gen(diff_ask):
    height = random.randint(1, 10)
    width = random.randint(1, 10)
    base = random.randint(1, 10)
    radius = random.randint(1, 10)

    if diff_ask == "easy":
        area = height * width
        print("If the height of the square/rectangle is {} and the width is {}, find the area.".format(height, width))
    elif diff_ask == "medium":
        area = 0.5 * base * height
        print("Find the area of a triangle if the base is {} and the height is {}.".format(base, height))
    elif diff_ask == "hard":
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
    print("====================================")
    print("Welcome to the Area Calculator Game!")
    print("====================================")
    print()

    played_before = user_response_checker("Would you like to see the instructions? ", yesno_list)

    if played_before == "yes":
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

    formula_check = user_response_checker("Would you like to see the formula list? ", yesno_list)

    if formula_check == "yes":
        print()
        print("The formula for finding the area of a SQUARE is: area = height * width")
        print("The formula for finding the area of a TRIANGLE is: area = 0.5 * base * height")
        print("The formula for finding the area of a CIRCLE is: area = PI * radius^2")
        print("================================")
        print("PI is set as *3.14* in this game")
        print("================================")

    diff_ask = user_response_checker("Which difficulty would you like to play? ", questiondiff_list)

    if diff_ask == "exit":
        return

    print("------------------------------------")
    print("You have chosen the {} difficulty!".format(diff_ask))
    print("------------------------------------")

    question_right = 0
    question_wrong = 0

    question = None
    if diff_ask != "xxx":
        question = user_response_checker("How many QUESTIONS would you like to play (press enter for infinite Question): ")

    question_played = 0
    while not question or question_played < int(question):
        print()
        if not question:
            heading = "Continuous Mode: Question {}".format(question_played + 1)
        else:
            heading = "!Question {} of {}!".format(question_played + 1, question)
        print(heading)
        result = question_gen(diff_ask)
        if result == "exit":
            break
        if result == "right":
            question_right += 1
        else:
            question_wrong += 1
        question_played += 1

    # Calculate Game Stats
    question_played = question_right + question_wrong
    percent_right = question_right / question_played * 100
    percent_wrong = question_wrong / question_played * 100

    print()
    # Displays game stats with % values to the nearest whole number
    print("===== Game Statistics =====")
    print("Questions Played: {}".format(question_played))
    print(f"Right: {question_right}, ({percent_right:.0f}%) \nLose: {question_wrong}, ({percent_wrong:.0f}%)")

# Call the play_game() function
play_game()
