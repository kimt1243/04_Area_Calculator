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

        # output error if item not in list
        print("Please type either yes or no")