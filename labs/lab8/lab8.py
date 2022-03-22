"""
Name: Ben Kelehear
lab8.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from time import sleep
from random import randint
from graphics import *

def bumper():

    #_______Set-Up_______
    width = 400
    height = 400
    win = GraphWin("Bumper", width, height)
    close_pt = Point(width / 2, height - 10)
    close = Text(close_pt, "Bumper Cars :D")
    close.draw(win)

    #________Circle 1________
    circle_1 = Circle(Point(160, 50), 25)
    circle_1.setOutline(get_random_color())
    circle_1.setFill(get_random_color())
    circle_1.draw(win)

    #________Circle 2________
    circle_2 = Circle(Point(200, 200), 25)
    circle_2.setOutline(get_random_color())
    circle_2.setFill(get_random_color())
    circle_2.draw(win)

    #_______Movement_________
    dx1 = get_random(25)
    dx2 = get_random(25)
    dy1 = get_random(15)
    dy2 = get_random(15)
    while win.checkMouse() is None:
        circle_1.move(dx1, dy1)
        circle_2.move(dx2, dy2)
        sleep(0.03)
    win.close()

def get_random(move_amount):
   make_move = randint(-move_amount, move_amount)
   return make_move


def did_collide(circle_ball, circle_ball2):
    circle1_radius = circle_ball.getRadius()
    circle2_radius = circle_ball2.getRadius()
    if circle1_radius == circle2_radius:
        return True
    else:
        return False


def hit_vertical(circle_ball, win):
    win_width = win.getWidth()
    circle_radius = circle_ball.getRadius()
    x_pos = circle_ball.getCenter().getX()
    if circle_radius < x_pos < win_width - circle_radius:
        return False
    else:
        return True


def hit_horizontal(circle_ball, win):
    win_height = win.getHeight()
    circle_radius = circle_ball.getRadius()
    y_pos = circle_ball.getCenter().getY()
    if circle_radius < y_pos < win_height - circle_radius:
        return False
    else:
        return True


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color_fill = color_rgb(red, green, blue)
    return color_fill


bumper()