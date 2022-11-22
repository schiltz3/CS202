# Write a function named countString which should take a string filename and a string s as parameters and return the number
# of times the string s is present in the file with the name filename. Once you have tested the countString function,
# write a main function which should ask the user for a file's name and a string and print how many times the string is
# present in that file. The main function MUST call the countString function you wrote. Both the functions should be in
# the same program file. Submit the program file.

# Hints: Use one of the functions for reading which will be easiest for this task. Use the string function "count"
# (you can refer to the strings slides for how to use it).


def countString(filename, s) -> int:
    total = 0
    with open(filename) as file:
        for line in file:
            total += line.count(s)
    return total


if __name__ == "__main__":
    try:
        filename = str(input("Enter Filename"))
        str = str(input("Enter String"))
    except Exception as e:
        print("Please input")

    occurrences = countString(filename, str)

    print(f"Number of occurrences of {str} in {filename} is: {occurrences}")
