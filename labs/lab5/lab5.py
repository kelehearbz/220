"""
Name: Ben Kelehear
lab5.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Belle Fortson
"""

import math
from graphics import *

def triangle():
    width = 500
    height = 500
    win = GraphWin("triangle", width, height)
    instruction_loc = Point(width / 2, height - 50)
    instruction = Text(instruction_loc, "Click 3 points to draw triangle")
    instruction.draw(win)
    click = 4
    for r in range(click):
        click_user1 = win.getMouse()
        click_user2 = win.getMouse()
        click_user3 = win.getMouse()
        p1 = click_user1
        p1.draw(win)
        p2 = click_user2
        p2.draw(win)
        p3 = click_user3
        p3.draw(win)
        shape = Polygon(p1, p2, p3)
        shape.setFill("pink")
        shape.setOutline("pink")
        shape.draw(win)

        line1x = p2.getX() - p1.getX()
        line1y = p2.getY() - p1.getY()
        line2x = p3.getX() - p2.getX()
        line2y = p3.getY() - p2.getY()
        line3x = p1.getX() - p3.getX()
        line3y = p1.getY() - p3.getY()

        line1 = math.sqrt((line1x ** 2) + (line1y ** 2))
        line2 = math.sqrt((line2x ** 2) + (line2y ** 2))
        line3 = math.sqrt((line3x ** 2) + (line3y ** 2))

        perimeter = line1 + line2 + line3
        s = perimeter / 2
        area = math.sqrt(s * ((s - line1) * (s - line2) * (s - line3)))
        text1 = Text(Point(100, 80), "The Perimeter is: " + str(perimeter))
        text2 = Text(Point(100, 120), "The Area is: " + str(area))
        text1.draw(win)
        text2.draw(win)

        instruction.setText('Click anywhere to quit.')

    win.getMouse()
    win.close()

triangle()


def color_shape():

        # create window
        win_width = 400
        win_height = 400
        click = 5
        win = GraphWin("Color Shape", win_width, win_height)
        win.setBackground("white")

        # create text instructions
        msg = "Enter color values between 0 - 255\nClick window to color shape"
        inst = Text(Point(win_width / 2, win_height - 20), msg)
        inst.draw(win)

        # create circle in window's center
        shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
        shape.draw(win)

        # redTexPt is 50 pixels to the left and forty pixels down from center
        red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
        red_text = Text(red_text_pt, "Red: ")
        red_text.setTextColor("red")
        red_entry_pt = red_text_pt.clone()
        red_entry_pt.move(40, 0)
        red_entry = Entry(red_entry_pt, 5)
        red_entry.draw(win)

        # green_text_pt is 30 pixels down from red
        green_text_pt = red_text_pt.clone()
        green_text_pt.move(0, 30)
        green_text = Text(green_text_pt, "Green: ")
        green_text.setTextColor("green")
        green_entry_pt = green_text_pt.clone()
        green_entry_pt.move(40, 0)
        green_entry = Entry(green_entry_pt, 5)
        green_entry.draw(win)

        # blue_text_pt is 60 pixels down from red
        blue_text_pt = red_text_pt.clone()
        blue_text_pt.move(0, 60)
        blue_text = Text(blue_text_pt, "Blue: ")
        blue_text.setTextColor("blue")
        blue_entry_pt = blue_text_pt.clone()
        blue_entry_pt.move(40, 0)
        blue_entry = Entry(blue_entry_pt, 5)
        blue_entry.draw(win)

        # display rgb text
        red_text.draw(win)
        green_text.draw(win)
        blue_text.draw(win)

        for i in range(click):
            win.getMouse()
            r = int(red_entry.getText())
            g = int(green_entry.getText())
            b = int(blue_entry.getText())
            shape.setFill(color_rgb(r, g, b))

        # Wait for another click to exit
        win.getMouse()
        win.close()

color_shape()

def process_string():
    print("Hi! Please enter your string below :)")
    user_str = input("")
    # __First letter__
    print(user_str[0])
    # __Last letter__
    print(user_str[-1])
    # __Position__ 2-5
    print(user_str[1:5])
    # __Concatenation__
    first_letter = user_str[0]
    last_letter = user_str[-1]
    concatenation = first_letter + last_letter
    print(concatenation)
    # __First 3 chars repeated 10 times
    first_three = user_str[0:4]
    times_ten = first_three * 10
    print(times_ten)
    # __Print one character per line  ???
    for i in (user_str):
        print(i)
    # __Num of characters__
    print(len(user_str))

process_string()



def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    q = float(values[5])
    x = [values[2], values[0], q]
    print(x)
    r = float(values[5])
    x = values[0] + values[2] + r
    print(x)
    x = len(values)
    print(x)


process_list()


def another_series():
    num_term = eval(input('Enter the number of terms:'))
    acc = 0
    term = 0
    for i in range(num_term):
        term = term % 6
        term += 2
        acc = acc + term

        print(term, end=' ')

    print("\nSum = ", acc, )

another_series()

def target():
    width = 500
    height = 500
    win = GraphWin("target", width, height)
    radius = 50
    circle1 = Circle(Point(width / 2, height / 2), radius + 200)
    circle2 = Circle(Point(width / 2, height / 2), radius + 150)
    circle3 = Circle(Point(width / 2, height / 2), radius + 100)
    circle4 = Circle(Point(width / 2, height / 2), radius + 50)
    circle5 = Circle(Point(width / 2, height / 2), radius)

    circle1.setFill('white')
    circle2.setFill('black')
    circle3.setFill('blue')
    circle4.setFill('red')
    circle5.setFill('yellow')

    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    circle4.draw(win)
    circle5.draw(win)
    instruction_loc = Point(width / 2, height - 30)
    instruction = Text(instruction_loc, "Click to close")
    instruction.draw(win)

    win.getMouse()
    win.close()

target()