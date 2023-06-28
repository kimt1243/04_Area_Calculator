# Lists
yesno_list = ["yes", "no", "xxx"]

def yes_no_checker(question):
    while True:
        # Ask user for choice
        response = input(question).lower()

        # Check if response is in the list of valid choices (full name or first letter)
        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please type either 'yes', 'no', or 'xxx'")

def instructions():
    print()
    print("**** Area Calculator Game ****")
    print()
    print("For each game, you will be asked to:")
    print()
    print("- Choose a difficulty for your math question.")
    print("  - Easy mode contains squares. ")
    print("  - Medium mode contains triangles, squares. ")
    print("  - Hard mode contains circles, triangles, squares. ")
    print("- Enter the number of rounds (or press enter for infinite rounds) that you want to play.")
    print("- You will be given 3 guesses to answer each question.")
    print("- Can you guess the correct area?")
    print()
    return ""

def formula_checker(question):
    while True:
        # Ask user for choice
        response = input(question).lower()

        if response == 'xxx':
            return 'xxx'

        print("Please type a valid formula (square, triangle, circle), or 'xxx' to end the game\n")

# Check if user wants to see the instructions
played_before = yes_no_checker("Would you like to see the instructions? ")

if played_before == "xxx":
    print("You have chosen 'xxx'. Thank you for playing!")
    exit()  # Use exit() to end the program

if played_before == "yes":
    instructions()

# Check if user wants to see the formula list
formula_check = yes_no_checker("Would you like to see the formula list? ")

if formula_check == "xxx":
    print("You have chosen 'xxx'. Thank you for playing!")
    exit()  # Use exit() to end the program

if formula_check == "yes":
    print()
    print("The formula for finding the area of a square is: area = height * width")
    print()
    print("The formula for finding the area of a triangle is: area = height * base * 0.5")
    print()
    print("The formula for finding the area of a circle is: area = PI * radius^2")
