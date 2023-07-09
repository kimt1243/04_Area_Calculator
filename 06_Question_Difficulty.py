# Functions go here...
questiondiff_list = ["easy", "medium", "hard", "xxx"]

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


# Main Routine goes here...
diff_ask = difficulty_checker("Which difficulty would you like to play? ")

if diff_ask == "easy":
    print()
    print("Easy difficulty has been chosen")
if diff_ask == "medium":
    print()
    print("Medium difficulty has been chosen")
if diff_ask == "hard":
    print()
    print("Hard difficulty has been chosen")
if diff_ask == "xxx":
    print()
    print("You have chosen 'xxx', Thank you for playing!")
    exit()


