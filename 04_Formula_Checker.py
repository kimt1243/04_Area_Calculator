import math

def formula_checker():
    while True:
        response = input("Choose the formula of a shape you want to know: (square, triangle, or circle "
                         "(or 'xxx' to exit): ").lower()

        if response == 'xxx':
            break

        shape = response[0]  # Get the first letter of the shape

        if shape == 's':
            try:
                print("The formula for finding a square is: area = height * width")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif shape == 't':
            try:
                height = float(input("Enter height of triangle: "))
                base = float(input("Enter base of triangle: "))
                area = 0.5 * height * base
                print("Area of triangle:", area)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif shape == 'c':
            try:
                radius = float(input("Enter radius of the circle: "))
                area = math.pi * radius ** 2
                print("Area of circle:", area)
            except ValueError:
                print("Invalid input. Please enter a number.")

        else:
            print("Please enter a valid shape: square, triangle, or circle.")


# Main routine goes here

formula_checker()