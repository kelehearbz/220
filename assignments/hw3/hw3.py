"""
Name: Ben Kelehear
hw3.py

Problem: Homework 3

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def average():
    grades = eval(input("Hello! How many grades do you have? "))
    average_acc = 0
    for i in range(grades):
        user_input = eval(input("Enter a grade here: "))
        average_acc = average_acc + user_input
        average = average_acc / grades
    print("Your average is: ", average)


def tip_jar():
    num_people = 5
    tip_acc = 0
    for i in range(num_people):
        tips = eval(input("Please enter your tip amount: "))
        tip_acc = tip_acc + tips
        tip_total = tip_acc
    print("Total tips: ", tip_total, " Thank you for your generosity! :)")


def newton():
    user_number = eval(input("What number do you wish to square root? "))
    user_approx = eval(input("How many times do you want to improve the approximation? "))
    approx = 0.5 * user_number
    for j in range(user_approx):
        approx_square = 0.5 * (approx + user_number / approx)
    print("The square root is approximately ", approx_square)


def sequence():
    terms = eval(input("How many terms would you like? "))
    for j in range(1, 9):
        print((j % terms, end=" ")




def pi():
    t_series = eval(input("How many terms are in the series? "))
    for k in range(1, 9):
        print(k %2 + k-1)


if __name__ == '__main__':
    pass
