"""
Name: Ben Kelehear
lab7.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(input_file_name, output_file_name):
    open_grades = open(input_file_name, "r")
    grade_list = open_grades.readlines()
    for line in grade_list:
        acc = 0
        weight_acc = 0
        line_split = line.split(":")
        num_list = line_split[1].split()
        for i in range(0, len(num_list), 2):
            acc = acc + int(num_list[i]) * int(num_list[i + 1])
            weight_acc = weight_acc + int(num_list[i])
        average = acc / 100
        if weight_acc > 100:
            print(line_split[0], "'s average: ", "Error! The weights are more than 100.")
        elif weight_acc < 100:
            print(line_split[0], "'s average: ", "Error! The weights are less than 100.")
        else:
            print(line_split[0], "'s average: ", average)
    class_avg = average
    print("The class average is: ", class_avg)




def main():
    weighted_average("grades.txt", "avg.txt")


main()

# sum of averages divided by number of applicable students