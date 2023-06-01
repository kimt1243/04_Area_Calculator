# Functions go here


def round_checker():
    while True:
        response = input("How many rounds would you like to play (enter for infinite rounds) : ")

        response_error = ("Please type either <enter> or and integer "
                          "that is more than 0")

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
choose_instruction = "Please type a whole number bigger and equal to 1"

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