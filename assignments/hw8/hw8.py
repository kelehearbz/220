"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def add_ten(nums):
    num_split = num_list.split(" ")
    for i in range(0, len(num_split)):
        num_split[i] = eval(num_split[i])
    solution = num_split[0] + 10, num_split[1] + 10, num_split[2] + 10
    print(solution)

def square_each(nums):
    num_split = num_list.split(" ")
    for i in range(0, len(num_split)):
        num_split[i] = eval(num_split[i])
    solution = num_split[0] ** 2, num_split[1] ** 2, num_split[2] ** 2
    print(solution)


def sum_list(nums):
    num_split = num_list.split(" ")
    acc = 0
    for i in range(0, len(num_split)):
        num_split[i] = eval(num_split[i])
        num_acc = acc + num_split
    print(num_acc)




def to_numbers(nums):
    num_split = num_list.split(" ")
    for i in range(0, len(num_split)):
        num_split[i] = eval(num_split[i])
    print(num_split)




def sum_of_squares(nums):
    num_split = num_list.split(" ")
    for i in range(0, len(num_split)):
        num_split[i] = eval(num_split[i])
    solution = num_split[0] ** 2 + num_split[1] ** 2 + num_split[2] ** 2
    print(solution)


def starter(weight, wins):
    if player_wt >= 199:
        print("Congrats! You are the required weight.")
    elif player_wins > 20:
        print("Congrats! You have enough wins.")
    else:
        print("Sorry, you do not meet the requirements.")


def leap_year(year):
    year = 345
    leap = year / 4
    print(leap)



def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    if circle_overlap > 20:
        print("false")


if __name__ == '__main__':
    circle1 = 15
    circle2 = 20
    did_overlap(circle1, circle2)
    year = 345
    leap_year(year)
    num_list = "1 2 3"
    add_ten(num_list)
    square_each(num_list)
    to_numbers(num_list)
    player_wt = eval(input("How much does the player weigh?: "))
    player_wins = eval(input("How many wins does the player have?: "))
    starter(player_wt, player_wins)
