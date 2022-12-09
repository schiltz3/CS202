# John Schiltz

# 1. Write a function addLists that takes two lists of numbers (assumed to be of equal length)
# and returns another list which has each element as the sum of the corresponding
# elements of the two lists. For example, if the two lists are [2,3,4] and [3,1,1]
# then the returned list should be [5,4,5].
# The function should check that the two lists are of equal length before proceeding
# otherwise should print a message if they are not equal.
def addLists(l1: list, l2: list) -> list:
    if len(l1) != len(l2):
        print("Length of list are not equal")
    return [v1 + v2 for v1, v2 in zip(l1, l2)]


list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 4, 3, 2, 1]
long_list = [1, 2, 3, 4, 5, 6]
print(addLists(list_1, list_2))
print(addLists(list_1, long_list))

# 2. Write a function makeDict that takes a list as an argument and returns a dictionary
# such that its keys are the elements of the list and the values
# are the number of  times the element is present.
# For example, if the list is [10, 5, 10, 4, 5, 10] then the returned dictionary should be
# {10:3, 4:1, 5:2} (the order does not matter).


def makeDict(l: list) -> dict:
    accumulator = {}
    for element in l:
        accumulator[element] = accumulator.get(element, 0) + 1
    return accumulator


list_dict_1 = [10, 5, 10, 4, 5, 10]
print(makeDict(list_dict_1))
