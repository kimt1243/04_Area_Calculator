# Functions go here...
Formula_list = ["square", "triangle", "circle"]
yesno_list = ["yes", "no"]

# Functions go here


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
    print("**** Area Calculator Game ****")
    print()
    print("For each game you will be asked to...")
    print()
    print("-Choose a difficulty for your math question "
          "\n   Easy mode contains squares and rectangles. "
          "You will only be asked to find the area. "
          "\n   Medium mode contains triangles, squares and rectangles. "
          "You wil also be asked to find the height, width of the shape "
          "\n   Hard mode contains circles, triangles, squares and rectangles. "
          "You wil also be asked to find the height, width of the shape")

    print("-Enter the number of rounds (enter for infinite rounds) that you want to play.")
    print("-The user will be given 3 guesses to answer the question. ")

    print("-Can you ")
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
            print("please type a valid formula (square, triangle, circle)")
            print()


questiondiff_list = ["easy", "medium", "hard"]

# Functions go here


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
            print("please type a valid difficulty (easy, medium, hard)")
            print()


def round_checker():
    while True:
        response = input("How many rounds would you like to play (enter for infinite rounds) : ")

        response_error = ("Please type either <enter> or and integer "
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


played_before = yes_no_checker("Would you like to see the instructions? ")

if played_before == "yes":
    instructions()
formula_check = yes_no_checker("Would you like to see the formula list? ")

if formula_check == "yes":
    print()
    print("The formula for finding the area of a square is: {area = height * width}")
    print()
    print()
    print("The formula for finding the area of a triangle is: {area = height * base * 0.5}")
    print()
    print()
    print("The formula for finding the area of a circle is: {area = PI * radius ^ 2}")
    print()

diff_ask = difficulty_checker("Which difficulty would you like to play? ")

if diff_ask == "easy":
    print()
    print("you have chosen easy")
    print()
if diff_ask == "medium":
    print()
    print("you have chosen medium")
    print()
if diff_ask == "hard":
    print()
    print("you have chosen hard")
    print()


rounds_played = 0
choose_instruction = "Please type a whole number bigger or equal to 1"

# Ask user for # of rounds, <enter> for infinite mode
rounds = round_checker()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    # End game if exit code is typed
    if choose == "xxx":
        break
    # rest of loop / game
    print("You chose {}".format(choose))

    rounds_played += 1

# End game if number of rounds < number of rounds played
    if rounds_played == rounds:
        print("Thank you for playing")
        break