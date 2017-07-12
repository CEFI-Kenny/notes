
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



# use requests module to download content
import requests

# download a text file and store in res
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# res.status_code == 200


# res = requests.get("https://inventwithpython.com/page_that_does_not_exist")
# res.status_code == 404


# detect bad download in order to make sure that download actually work
try:
    res.raise_for_status()
    print("no error")
except Exception as exception:
    print("There was a problem: %s" % (exception))

"""
# write web content to a text file
text_file = open("text_file.txt", "wb") # must be write binary
# iterate over 1000 bytes at a time
for chunk in res.iter_content(1000):
    # print(char)
    # not necessaryly assign the return value of file.write() to a variable
    num_bytes_wrote = text_file.write(chunk)
    print(num_bytes_wrote)
text_file.close()
"""


