"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import Point, GraphWin, Circle, Text, Entry, Rectangle

def squares():

    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Squares", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        shape = Rectangle(Point(50, 50), Point(20, 20))
        center = shape.getCenter()  # center of circle
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

    win.getMouse()
    win.close()

    input(" ")


def rectangle():

    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    num_clicks = 1

    for i in range(num_clicks):
        click = win.getMouse()
        shape2 = Rectangle(Point(50, 50), Point (50, 50))
        center = shape2.getCenter()  # center of circle
        shape2.setOutline("orange")
        shape2.setFill("orange")
        shape2.draw(win)
        perimeter_formula = 50 / 50
        perimeter_pt = Point(width / 2, height - 25)
        perimeter = Text(perimeter_pt, "The perimeter is 25")
        perimeter.draw(win)
        area_pt = Point(width / 2, height - 40)
        area = Text(close_pt, "The area is")
        area.draw(win)
        perimeter.draw(win)
        close_pt = Point(width / 2, height - 10)
        close = Text(close_pt, "Click again to close =)")
        close.draw(win)

        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape2.move(change_x, change_y)

    win.getMouse()
    win.close()

    input(" ")


def circle():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    num_clicks = 1

    for i in range(num_clicks):
        click = win.getMouse()
        shape2 = Circle(Point(50, 50), 50)
        center = shape2.getCenter()  # center of circle
        shape2.setOutline("yellow")
        shape2.setFill("yellow")
        shape2.draw(win)
        radius_formula = 50 / 2
        radius_pt = Point(width / 2, height - 25)
        radius = Text(radius_pt, "The radius is 25")
        radius.draw(win)
        close_pt = Point(width / 2, height - 10)
        close = Text(close_pt, "Click again to close =)")
        close.draw(win)


        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape2.move(change_x, change_y)

    win.getMouse()
    win.close()

    input(" ")

def pi2():
    pass


if __name__ == '__main__':
    pass
