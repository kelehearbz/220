"""
Name: Ben Kelehear
hw9.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def get_words(file_name):
    file = open(file_name, "r")
    file_read = file.readlines()
    file_string = file_read.str()
    print(file_string)
get_words("hangman.txt")


# def get_random_word(words):
#     pass
#
#
# def letter_in_secret_word(letter, secret_word):
#     pass
#
#
# def already_guessed(letter, guesses):
#     pass
#
#
# def make_hidden_secret(secret_word, guesses):
#     pass
#
#
# def won(guessed):
#     pass
#
#
# def play_graphics(secret_word):
#     pass
#
#
# def play_command_line(secret_word):
#     pass
#
#
# if __name__ == '__main__':
#     pass
#     # play_command_line(secret_word)
#     # play_graphics(secret_word)
