# Functions go here

def round_checker():
    while True:
        response = input("How many rounds would you like to play (enter 'xxx' to end): ")

        response_error = "Please type either 'xxx' or an integer that is a whole number and more than 0"

        if response.lower() == "xxx":
            return "xxx"

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


# Main routine goes here


rounds_played = 0
choose_instruction = "Enter your guess"

# Ask user for # of rounds, 'xxx' to end the game
rounds = round_checker()

if rounds == "xxx":
    print("Thank you for playing!")
else:
    end_game = "no"
    while end_game == "no":
        # Rounds Heading
        print()
        if rounds == "":
            heading = "Continuous Mode: Question {}".format(rounds_played + 1)
        else:
            heading = "Question {} of {}".format(rounds_played + 1, rounds)

        print(heading)
        choose = input("{} or 'xxx' to end: ".format(choose_instruction))

        # End game if exit code is typed
        if choose == "xxx":
            break

        # Rest of the loop / game
        print("You chose {}".format(choose))
        rounds_played += 1

        # End game if number of rounds < number of rounds played
        if rounds_played == rounds:
            print("Thank you for playing")
            break