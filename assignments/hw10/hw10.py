"""
Name: Ben Kelehear
hw10.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sphere import Sphere
from face import Face

def fibonacci(n):
    while n < 1:
        print("Sorry, that input is incorrect :(")
        return None
    fibo = n - 1
    print(fibo)
    return fibo

fibonacci(eval(input("enter your number: ")))

def double_investment(principle, rate):
    principle_conv = float(principle)
    rate_conv = float(rate)
    a = principle_conv  * (1 + rate_conv)
    print(a)
    return a

double_investment(eval(input("Enter your starting investment value: ")), eval(input("Enter your annualized interest rate: ")))

def syracuse(n):
    syr_even = n / 2
    syr_even_2 = syr_even / 2
    syr_even_3 = syr_even_2 / 2
    syr_even_list = syr_even, syr_even_2, syr_even_3
    syr_odd = 3 * n + 1
    syr_odd_2 = 3 * syr_odd + 1
    syr_odd_3 = 3 * syr_odd_2 + 1
    syr_odd_list = syr_odd, syr_odd_2, syr_odd_3
    print(syr_even_list)
    print(syr_odd_list)
    return syr_even_list, syr_odd_list
syracuse(eval(input("Enter your number: ")))

def goldbach(n):
    while 2 > n:
        print("sorry, that is invalid :(")
        return None
    print(n, 3, 8)
goldbach(eval(input("Enter a number: ")))

def sphere():
    return None

def face():
    return None
