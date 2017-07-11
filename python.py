# teriminate a program
import sys
sys.exit()



# import pyperclip in order to get access to clip board
import pyperclip

# copy to clip board
pyperclip.copy("some text here")
# paste from clip board
content_in_clip_board = pyperclip.paste()



# import shell utility module
import shutil
