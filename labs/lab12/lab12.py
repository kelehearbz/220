"""
Name: Ben Kelehear
lab12.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        if value == list[i]:
            list.pop(i)
            list.insert(i, "Ben")
            i = len(list)
        i += 1

def main():
    my_list = ["Red", "Orange", "Yellow", "Green"]
    find_and_remove_first(my_list, "Red")

if __name__ == '__main__':
    main()