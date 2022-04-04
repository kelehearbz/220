"""
Name: Ben Kelehear
lab4.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
from button import Button
from door import Door

def main():
    # __ Setup __
    running = True
    width = 600
    height = 600
    win = GraphWin("Door Simulator", width, height)
    win.setBackground(color_rgb(245, 244, 179))

    # __Door__
    box1 = Rectangle(Point(150, 250), Point(470, 600))
    door = Door(box1, "Closed")
    door.color_door("red")
    door.draw(win)

    # __Button__
    box2 = Rectangle(Point(100, 50), Point(500, 200))
    button = Button(box2, "Bye-bye!")
    button.color_button(color_rgb(117, 148, 137))
    button.draw(win)

    while running:
        click = win.getMouse()
        if button.is_clicked(click):
            break
        elif door.is_clicked(click):
            status = door.get_label()
            if status == "Open":
                door.close("red", "Closed")
            else:
                door.open("white", "Open")

    win.close()


if __name__ == '__main__':
    main()
