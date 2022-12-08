from random import randint


def game():
    _continue = str(input("Do you want to play the game of adding two numbers? y/n ")).lower()
    if _continue != "y":
        return
    while _continue != "n":
        rand_1 = randint(1, 100)
        rand_2 = randint(1, 100)

        print(f"The two numbers are {rand_1} and {rand_2}")

        g_sum = int(input("What is the sum of the two numbers? "))
        if g_sum == rand_1 + rand_2:
            print("Your answer is correct!")

        while g_sum != rand_1 + rand_2:
            print("Your answer is incorrect.")
            g_sum = int(input("What is the sum of the two numbers? "))
            if g_sum == rand_1 + rand_2:
                print("Your answer is correct!")

        _continue = str(input("Do you want to play the game again? y/n "))


if __name__ == "__main__":
    game()
