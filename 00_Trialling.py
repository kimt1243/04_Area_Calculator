# Boolean or String?
def intfloat_checker(question, exit_code=None, allow_floats=True):

    while True:
        response = input(question)

        if response == exit_code:
            return None

        elif response != "":
            try:
                if allow_floats:
                    response = float(response)

                    if response < 1:
                        print("Please input a valid Number over '1'\n")
                        continue

                elif not allow_floats:
                    response = int(response)

                    if response < 1:
                        print("Please input a valid Number over '1' \n")
                        continue

            except ValueError:
                print("<Error> That is an invalid Integer / Number\n")
                continue

        return response
