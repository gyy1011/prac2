def determine_status(score):
    """different score and get different result"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    MENU = """
    G - get a valid score 
    P - print result 
    S - show stars 
    Q - quit"""
    print(MENU)
    choice = input(">>> ").upper()
    score = None
    status = None
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            status = determine_status(score)
            while status == "Invalid score":
                print("Invalid score")
                score = float(input("Enter score: "))
                status = determine_status(score)
        elif choice == "P":
            if score is None:
                print("pls input score first, use G")
            else:
                print(status)
        elif choice == "S":
            if score is None:
                print("pls input score first, use G")
            else:
                print('*' * int(score))
        else:
            print("Invalid input")

        print(MENU)
        choice = input(">>> ").upper()
    print("Thank U!")


main()