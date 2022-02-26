"""
Name: Ben Kelehear
hw6.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def cash_converter():
    user_input = input("Enter an integer: ")
    value = float(user_input)
    print("That is ", round(value, 2), end="0")


def encode():
    str = input("Enter a message: ")
    key = input("Enter a key: ")
    print(str.replace("a", "d", key))


def sphere_area(radius):
    user_radius = input("Please enter your sphere radius: ")
    radius = float(user_radius)
    area = 4 * math.pi * radius ** 2
    print("The sphere area is ", round(area, 2))


def sphere_volume(radius):
    user_radius = input("Please enter your sphere radius: ")
    radius = float(user_radius)
    sphere_volume = 4 / 3 * math.pi * radius ** 3
    print("The sphere volume is ", round(sphere_volume, 2))

def sum_n(number):
    sum_n = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    number = float(sum_n)
    print("Sum of n is ", number)


def sum_n_cubes(number):
    sum_n_cubes = 1 + 2 ** 3 + 3 ** 3 + 4 ** 3 + 5 ** 3 + 6 ** 3 + 7 ** 3 + 8 ** 3 + 9 ** 3 + 10 ** 3
    number = float(sum_n_cubes)
    print("Sum of n cubes is ", number)


def encode_better():
    string = input("Enter a message: ")
    key = input("Enter a key: ")
    print(string.replace("a", "ace", key))


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
