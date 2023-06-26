max_guess = 3


def guess_compare(question):
    remaining_guesses = max_guess

    while remaining_guesses > 0:
        print("Remaining guesses:", remaining_guesses)
        response = input(question)
        response_error = "Please type a positive integer."

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(response_error)
                    continue

                remaining_guesses -= 1

                if response == secret_number:
                    print("Congratulations! You guessed the correct number.")
                    return True
                else:
                    print("Sorry, that's not the correct number.")

            except ValueError:
                print(response_error)
        else:
            print(response_error)

    print("You have used all your guesses. The correct number was", secret_number)
    return False


# Example usage
secret_number = 42
result = guess_compare("Guess the number: ")

if not result:
    print("Game over.")