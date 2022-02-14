"""
Name: Ben Kelehear
lab4.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import time
from graphics import Circle, GraphWin, Point, Text, Polygon, Rectangle

def bemine():

    #_______Set-Up_______
    width = 400
    height = 400
    win = GraphWin("Be Mine <3 <3", width, height)
    close_pt = Point(width / 2, height - 10)
    close = Text(close_pt, "Click again to close =)")
    close.draw(win)

    #________Text__________
    mine_pt = Point(width / 2, height - 45)
    mine = Text(mine_pt, "Be Mine <3")
    mine.draw(win)

    #____Arrow____
    arrow_head = Polygon(Point(100, 100), Point(80, 80), Point(80, 115))
    arrow_head.setOutline("black")
    arrow_head.setFill("black")
    arrow_head.draw(win)
    arrow_body = Rectangle(Point(80, 100), Point(0, 100))
    arrow_body.setOutline("black")
    arrow_body.setOutline("black")
    arrow_body.draw(win)

    #_______Heart__________

    heart_1 = Circle(Point(160, 100), 50)
    heart_1.setOutline("pink")
    heart_1.setFill("pink")
    heart_1.draw(win)
    heart_2 = Circle(Point(230, 100), 50)
    heart_2.setOutline("pink")
    heart_2.setFill("pink")
    heart_2.draw(win)
    heart_3 = Polygon(Point(115, 100), Point(193, 250), Point(280, 100))
    heart_3.setOutline("pink")
    heart_3.setFill("pink")
    heart_3.draw(win)

    for i in range(15):
        arrow_head.move(25, 0)
        arrow_body.move(25, 0)
        time.sleep(0.1)

    win.getMouse()
    win.close()

    input("")

bemine()