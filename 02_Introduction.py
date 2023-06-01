# Functions go here...
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
            print("please type either yes or no")

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
    return ""


# Main Routine goes here...
played_before = yes_no_checker("Have you played the game before? ")

if played_before == "no":
    instructions()

print()
print("program continues")