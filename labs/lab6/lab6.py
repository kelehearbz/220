"""
Name: Ben Kelehear
lab6.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Belle Fortson
"""

from graphics import *

def vigenere():
    #clicks = 1
    width = 500
    height = 500
    win = GraphWin ("Vigenere", width, height)
    win.setBackground("pink")

    # _____ Messages _____
    message_pt = Point(100, 100)
    message = Text(message_pt, "Put your message here! -> ")
    message.draw(win)

    keyword_pt = Point(100, 150)
    keyword = Text(keyword_pt, "Enter your keyword =)  -> ")
    keyword.draw(win)

    # ____ Text Boxes ____
    user_msg_entry_pt = Point(330, 100)
    user_msg_entry = Entry(user_msg_entry_pt, 30)
    user_msg_entry.draw(win)

    user_key_entry_pt = Point(330, 150)
    user_key_entry = Entry(user_key_entry_pt, 30)
    user_key_entry.draw(win)

    # ____ Button ____
    button = Rectangle(Point(200, 200), Point(280, 250))
    button.draw(win)

    button_txt_pt = Point(240, 225)
    button_txt = Text(button_txt_pt, "Encode :)")
    button_txt.draw(win)
    win.getMouse()

    # ____ Encoding ____
    acc = ""
    msg = user_msg_entry.getText()
    msg = msg.replace(" ", "")
    msg = msg.upper()
    key = user_key_entry.getText()
    key = key.upper()
    for j in range(len(msg)):
        msg_ord = ord(msg[j]) - 65
        key_ord = ord(key[j%len(key)]) - 65
        convert = (msg_ord + key_ord) % 26
        convert_ascii = chr(convert + 65)
        acc = (acc + convert_ascii)


    # ____ Interaction ____
    button.undraw()
    button_txt.undraw()
    result_pt = Point(250, 270)
    result = Text(result_pt, "Resulting Message:")
    conversion_pt = Point(260, 300)
    conversion = Text(conversion_pt, acc)
    conversion.draw(win)
    result.draw(win)
    close_txt_pt = Point(250, 400)
    close_txt = Text(close_txt_pt, "<3 Click anywhere to close <3")
    close_txt.draw(win)
    win.getMouse()
    win.close()

vigenere()

