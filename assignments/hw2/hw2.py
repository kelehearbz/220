"""
Name: Ben Kelehear
hw2.py

Problem: Homework 2

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?: "))
    my_range = range(3, upper_bound + 1, 3)
    print("Sum of threes is: ", list(my_range))



def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
    print()



def triangle_area():
    a = eval(input("Enter side a length: "))
    b = eval(input("Enter side b length: "))
    c = eval(input("Enter side c length: "))
    s = a + b + c / 2
    area = math.sqrt(s * s - a * s - b * s - c)
    print("The area of your triangle is: ", area, ":)")


def sum_squares():
    lower= eval(input("Please enter the lower range: "))
    upper = eval(input("Please enter the upper range: "))
    n = 1
    for i in range(lower, upper):
        n = base * n
    print(n)




def power():
    base = eval(input("Hello! Please enter your base number: "))
    exponent = eval(input("Now, enter your exponent: "))
    n = 1
    for i in range(n, exponent+1):
        n = base * n
    print(base, "^", exponent, "is: ", n)




if __name__ == '__main__':
    pass
