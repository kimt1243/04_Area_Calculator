# Functions go here...
Formula_list = ["square", "triangle", "circle"]

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

# Main Routine goes here...
formula_ask = formula_checker("Which formula would you like to know? ")

if formula_ask == "square":
    try:
        print()
        print("The formula for finding the area of a square is: {area = height * width}")
        print()
    except ValueError:
        print("Invalid input. Please enter a number.")

if formula_ask == "triangle":
    try:
        print()
        print("The formula for finding the area of a triangle is: {area = height * base * 0.5}")
        print()
    except ValueError:
        print("Invalid input. Please enter a number.")

if formula_ask == "circle":
    try:
        print()
        print("The formula for finding the area of a circle is: {area = PI * radius ^ 2}")
        print()
    except ValueError:
        print("Invalid input. Please enter a number.")



