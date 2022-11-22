# - Show calling each of the functions from the posted birthday.py file.
from birthday import happy, sing, main

# - Write a small useful function of your own (different from what we did in the class or lab)
# that takes at least one parameter and returns something and then show calling that function.
def def_a_usefully_function(n: int):
    return [i for i in range(n)]


if __name__ == "__main__":
    happy()
    sing("Me")
    main()

    ret = def_a_usefully_function(8)
    print(ret)
