"""
Name: Ben Kelehear
<hw1>.py

Problem: I was absent all last week due to covid concerns, so I apologize for any code that is unoptimized or incorrect.
I went through all the problems on HW1 and attempted to make programs that would solve each issue. They can be run
in the python console.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    shots = eval(input("Enter the total shots: "))
    player = eval(input("Enter how many shots the player made"))
    quotient = player / shots
    percentage = quotient * 100
    print(percentage)


def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    price = 10.50 * pounds
    shipping = pounds * 0.86
    overhead = 1.50
    total = price + shipping + overhead
    print("Your total is: ", total)


def kilometers_to_miles():
    distance = eval(input("How many kilometers did you travel? "))
    miles = distance * 0.621371
    print("You traveled ", miles, "miles")


if __name__ == '__main__':
    pass
