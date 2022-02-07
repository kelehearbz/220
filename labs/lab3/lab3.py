"""
Name: Ben Kelehear
lab3.py

Problem: This program will allow the user to calculate the average vehicles per day for roads. On top of that, it will also
calculate the total amount of vehicles traveled on all roads as well as average number of vehicles per road! <3

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def traffic():
    avg_acc = 0
    road = eval(input("Welcome! How many roads have been surveyed? "))
    for i in range(1, road + 1):
        road_acc = 0
        print("How many days was road", i, "surveyed?")
        days = eval(input(""))
        for j in range(1, days + 1):
            print("How many cars traveled on day", j, "?")
            cars = eval(input(""))
            road_acc = road_acc + cars
            avg_acc = avg_acc + cars
        avg = road_acc / days
        print("Average cars on road", i,"is", avg)
    total_avg = avg_acc / road
    print("Total number of vehicles on all roads is ", avg_acc)
    print("Average number of vehicles per road is", total_avg)

traffic()
