"""
Name: Ben Kelehear
hw9.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def get_words(file_name):
    file = open(file_name, "r")
    file_read = file.readlines()
    return file_read
get_words("hangman.txt")


def get_random_word(words):
    file = open(words, "r")
    file_read = file.readlines()
    print(file_read)

get_random_word("hangman.txt")
    

def letter_in_secret_word(letter, secret_word):
        file = open(letter, "r")
        file_read = file.readlines()
        print(file_read)

get_random_word("hangman.txt")


def already_guessed(letter, guesses):
    file = open(letter, "r")
    file_read = file.readlines()
    print(file_read)

get_random_word("hangman.txt")


def make_hidden_secret(secret_word, guesses):
    file = open(words, "r")
    file_read = file.readlines()
    print(file_read)

get_random_word("hangman.txt")


def won(guessed):
    file = open(guessed, "r")
    file_read = file.readlines()
    print(file_read)

get_random_word("hangman.txt")


def play_graphics(secret_word):
    file = open(secret_word, "r")
    file_read = file.readlines()
    print(file_read)

get_random_word("hangman.txt")


def play_command_line(secret_word):
    file = open(secret_word, "r")
    file_read = file.readlines()
    print(file_read)

get_random_word("hangman.txt")

if __name__ == '__main__':
    play_command_line(secret_word)
    play_graphics(secret_word)
