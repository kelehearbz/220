"""
Name: Ben Kelehear
hw7.py

Problem: I struggled a lot with this homework and took an extra day to focus on it, I apologize for errors and issues
that may come up.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    number_words_file = open("220/assignments/hw7/mytext.txt", "r")
    number_words_file.read()
    print("output.txt")

number_words("mytext.txt", "output.txt")


def hourly_wages(in_file_name, out_file_name):
    hourly_wages_file = open("220/assignments/hw7/hourly_wages.txt", "r")
    hourly_wages_file.read()
    print("hourly_wages_output.txt")

hourly_wages("hourly_wages.txt", "hourly_wages_output.txt")


def calc_check_sum(isbn):
    isbn = input("Please enter your isbn number: ")
    calculate = isbn * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
    print("Your ISBN number is", calculate)




def send_message(file_name, friend_name):
    message1 = open("220/assignments/hw7/message1.txt")
    print("larry.txt")

send_message("message1.txt", "larry.txt")


def encode():
    str = input("Enter a message: ")
    key = input("Enter a key: ")
    print(str.replace("a", "d", key))


def send_safe_message(file_name, friend_name, key):
    print("carrie.txt", key)

senc_safe_message("encryption.py", "carrie.txt", key)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    string = input("Enter a message: ")
    key = input("Enter a key: ")
    print(string.replace("a", "ace", key))


if __name__ == '__main__':
    pass
