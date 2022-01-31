"""
Name: Ben Kelehear
lab2.py

Problem: Today I made a program called "Mean-Machine"! It's responsible for helping the user to calculate their mean,
rms average, harmonic mean, and geometric mean. It will ask the user to input the numbers they're working with and will
calculate it automatically. :)

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def mean_machine():

    # _____Mean__________
    n = eval(input("Welcome to the Mean-Machine! Enter how many numbers you are working with: "))
    mean_acc = 0
    rms_acc = 0
    hm_acc = 0
    geo_acc = 1
    for i in range(n):
        user_input = eval(input("Please enter a number here: "))
        mean_acc = mean_acc + user_input
        rms_acc = rms_acc + user_input ** 2
        hm_acc = hm_acc + 1 / user_input
        geo_acc = geo_acc * user_input
    mean = mean_acc / n

    # _____Rms Average______

    rms_mean = rms_acc / n
    rms_average = math.sqrt(rms_mean)
    print("Your rms average is ", round(rms_average, 3))

    #_____Harmonic Mean______
    hm_mean = n / hm_acc
    print("Your harmonic mean is ", round(hm_mean, 3))

    #_____Geometric Mean_______
    geo_mean = geo_acc ** (1 / n)
    print("Your geometric mean is ", round(geo_mean, 3))



mean_machine()