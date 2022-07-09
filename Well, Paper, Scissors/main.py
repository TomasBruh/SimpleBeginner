import random
choices = ["well", "scissors", "paper"]
print("""Well > Scissors;  Scissors > Paper;  Paper > Well""")
programs_choice = random.choice(choices)
users_choice = input("What do yo choose? <-> ").lower()
print("")


def printer(outcome):
    print(f"Program chose: {programs_choice} \n"
          f"You chose: {users_choice}\n"
          f"You {outcome}")


if choices.__contains__(users_choice):
    if programs_choice == users_choice:
        printer("TIED")
    elif users_choice == "well":
        if programs_choice == "scissors":
            printer("WON")
        else:
            printer("LOST")
    elif users_choice == "paper":
        if programs_choice == "well":
            printer("WON")
        else:
            printer("LOST")
    elif users_choice == "scissors":
        if programs_choice == "well":
            printer("LOST")
        else:
            printer("WON")
else:
    print("There is no choice like that")
