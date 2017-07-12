
# teriminate a program
import sys
# sys.exit()



# import pyperclip in order to get access to clip board
import pyperclip

# copy to clip board
# pyperclip.copy("some text here")
# paste from clip board
content_in_clip_board = pyperclip.paste()



import os, webbrowser

# get command line arguments
# e.g. python3 python.py arg1 arg2
#      sys.argv = ["python.py", "arg1", "arg2"]

# check if there is at least one command line argument
if len(sys.argv) > 1:
    # form the address string without name of the program
    address = " ".join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

# e.g. python3 python.py 3221 North Service Road, Burlington, ON.
# webbrowser.open("https://www.google.com/maps/place/" + address)

