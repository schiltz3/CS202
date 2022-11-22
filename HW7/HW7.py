# - Play with Boolean operators listed in slide #34 on IDLE (like slide #38 of Part 1)

# - Run the posted vote.py program a few times

# - Write a short program that uses if-else statements nested to a depth of at least 3,
# similar to the vote.py program. Run it on IDLE with a few different inputs.
# Also submit the program (.py file) besides the IDLE screenshot.


def playing_with_bools():
    print("True" == True)
    print("str" < "nstr")
    print(0 == 0.00)
    print(0 == "0.00")
    print(0 == "0")
    pass


def short_program_using_nested():
    cereal = input("Do you have cereal? yes/no: ")
    if cereal == "yes":
        milk = input("Do you have milk? yes/no: ")
        if milk == "yes":
            bowls = int(input("How many bowls do you have? "))
            if bowls > 0:
                print("Congrats, you made cereal!")
            else:
                print("You need a bowl for cereal!")
        else:
            print("You need milk for cereal!")
    else:
        print("You need cereal for cereal!")


def short_program_using_guard_clauses():
    cereal = input("Do you have cereal? yes/no: ")
    if cereal == "no":
        print("You need cereal for cereal")
        return

    milk = input("Do you have milk? yes/no: ")
    if milk == "no":
        print("You need milk for cereal!")
        return

    bowls = int(input("How many bowls do you have? "))
    if bowls == 0:
        print("You need a bowl for cereal!")
        return

    print("Congrats, you made cereal!")


if __name__ == "__main__":
    playing_with_bools()
    short_program_using_nested()
    short_program_using_guard_clauses()
