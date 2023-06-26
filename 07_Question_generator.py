# Functions go here...
import random
questiondiff_list = ["easy", "medium", "hard"]



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
            print("please type either easy, medium or hard. ")
            print()

# Main Routine goes here...
diff_ask = difficulty_checker("Which difficulty would you like to play? ")

Question1 = "sq"
Question2 = "sq2"
Question3 = "tri"
Question4 = "tri2"
Question5 = "cir"
Question6 = "cir2"

def Question_gen():
    if diff_ask == "easy":
        print()
        print("you have chosen easy")
        print(random.randint(Question1, Question2))
    if diff_ask == "medium":
        print()
        print("you have chosen medium")
    if diff_ask == "hard":
        print()
        print("you have chosen hard")


