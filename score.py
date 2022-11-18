def main():
    """get a score and input."""
    score = float(input("Enter score: "))
    print(determine_status(score))


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


main()