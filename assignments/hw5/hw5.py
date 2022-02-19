"""
Name: Ben Kelehear
hw5.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def name_reverse():
    full_name = input("Enter your first and last name: ")
    rearrange = full_name.split(' ')
    name_1 = rearrange[0]
    name_2 = rearrange[1]
    print(name_2 + ",", name_1)



def company_name():
    domain = input("Enter your company's domain: ")
    domain_split = domain.split(".")
    comp_name = domain_split[1]
    print(comp_name)



def initials():
    students = eval(input("How many students are in your class?"))
    for i in range(1, students+1):
        print("What is student", i, "named?")
        student_names = input("")
        names_split = student_names.split(' ')
        names_1 = names_split[0]
        names_2 = names_split[1]
        initial_1 = names_1[0]
        initial_2 = names_2[0]
        print(initial_1, initial_2)


# Needs Work
def names():
    name_list = input("Enter a list of names: ")
    list_split = name_list.split(',')
    part_1 = list_split[0]
    part_2 = list_split[1]
    surname_split = part_1.split(' ')
    lastname_split = part_2.split(' ')
    surname_initial = surname_split[0]
    lastname_initial = lastname_split[1]
    print(surname_initial, lastname_initial)




def thirds():
    num_sentences = eval(input("How many sentences are you using? "))
    for k in range(1, num_sentences+1):
        print("Enter sentence", k, "here:")
        sentence = input("")
        c = sentence [0: -1: 3]
        print(c)




def word_average():
    user_sentence = input("Enter your sentence: ")
    sentence_split = user_sentence.split()
    word_avg = sum(len(word) for word in sentence_split) / len(sentence_split)
    print(word_avg)


def pig_latin():
    pig_sent = input("Enter your sentence to convert to pig latin: ")
    sent_split = pig_sent.split(' ')
    print(sent_split)


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
