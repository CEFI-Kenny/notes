
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

# import beautiful soup 4 (beautify HTML files)
import bs4

res = requests.get("http://nostarch.com")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
# beautify a file
# soup = bs4.BeautifulSoup("a file object")

# select all divs
divs = soup.select("div")

# select span elements within a div
span_in_div = soup.select("div span")

# select span elements immediately following a div with nothing in between
span_follow_div = soup.select("div > span")

# select element by id = author
id_author = soup.select("#author")

# select elements use CSS class = icon-bar
css_icon_bar = soup.select(".icon-bar")

# select input elements with an attribute name = any value
input_name = soup.select("input[name]")

# select input elements with an attribute type = button
input_button = soup.select('input[type="button"]')

# note: soup.select() returns bs4.element.Tag objects
# it has methods such as find_parents(), insert(), etc.


# bs4.element.Tag.attrs returns a dictionary of { attribute: value }
'''
str(input_name[0]) 
"""
    <input 
            class="form-control form-text" 
            id="edit-search-block-form--2" 
            maxlength="128" 
            name="search_block_form" 
            placeholder="Search" 
            size="15" 
            title="Enter the terms you wish to search for." 
            type="text" 
            value=""
    />
"""

input_name[0].attrs == 
{
    'title': 'Enter the terms you wish to search for.',
    'placeholder': 'Search',
    'class': ['form-control', 'form-text'], 
    'type': 'text', 
    'id': 'edit-search-block-form--2', 
    'name': 'search_block_form', 
    'value': '', 
    'size': '15', 
    'maxlength': '128'
}
'''

# get plain text from a tag
p_tag = soup.select("p")[0] 
# <p class="cart-block-items collapsed uc-cart-empty">There are no products in your shopping cart.</p>

text = p_tag.getText() # 'There are no products in your shopping cart.'

# get values by attribute name
p_tag.get("class") # ['cart-block-items', 'collapsed', 'uc-cart-empty']

# get non-existent attribute
p_tag.get("non-existent") # returns None





'''
# control chorme with selenium
import time
from selenium import webdriver


driver = webdriver.Chrome()

# open browser and go to Google.ca
driver.get('http://www.google.ca')

# pause the program for 5 seconds in order to show which page is opened in chrome
time.sleep(5) 

# find the serach box on Google home page
search_box = driver.find_element_by_id('lst-ib')

# input some text to search, e.g. cefi
search_box.send_keys('cefi')

# search
search_box.submit()

# pause antoher 5 seconds in order to see search results
time.sleep(5)

# close the browser
driver.quit()

# HTML code of the search box
"""
<input 
    class="gsfi" 
    id="lst-ib"
    maxlength="2048" 
    name="q" 
    autocomplete="off" 
    title="Search" 
    type="text" 
    value="" 
    aria-label="Search" 
    aria-haspopup="false" 
    role="combobox" 
    aria-autocomplete="both" 
    dir="ltr" 
    spellcheck="false" 
    style=" 
        border: none;
        padding: 0px; 
        margin: 0px; 
        height: auto; 
        width: 100%; 
        background: 
            url(&quot;data:image/gif;
            base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw%3D%3D&quot;
            ) transparent; 
        position: absolute; 
        z-index: 6; 
        left: 0px; 
        outline: none;
    ">
"""
'''

from selenium import webdriver

# find elements with selenium
browser = webdriver.Chrome()

browser.get('http://www.google.ca')

# find first occurrence of element with CSS class=class-name
# element = browser.find_element_by_class_name("class-name")

# find all elements with CSS class=class-name
# elements = browser.find_elements_by_class_name("class-name")

# other browser methods: find by id, partial_link_text, name, tag_name, etc



# methods for element found by browser.find() above

element = browser.find_element_by_id('lst-ib')

print(element.tag_name) # print input

browser.quit()