# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 01/31/2023
# Description: Modify insertion sort to sort a list of strings instead of numbers.
# It shouldn't return anything - it should sort the list "in place". The sorting should
# ignore case. After calling this function, the list that was passed in should now
# contain the exact same strings it did before, but in sorted order.

def string_sort(string_list):
    """Sorts string_list in alphabetical order."""
    for index in range(1, len(string_list)):
        word = string_list[index]
        pos = index - 1
        while (pos >= 0 and
               string_list[pos].lower() > word.lower()):
            string_list[pos + 1] = string_list[pos]
            pos -= 1
            string_list[pos + 1] = word


# list_1 = ["I", "wAnt", "to", "WorK", "in", "computer", "science"]
# string_sort(list_1)
# print(list_1)
