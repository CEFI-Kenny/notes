# teriminate a program
'''
import sys
# sys.exit()
'''


# import pyperclip in order to get access to clip board
'''
import pyperclip

# copy to clip board
# pyperclip.copy("some text here")
# paste from clip board
content_in_clip_board = pyperclip.paste()
'''


# webbrowser module
'''
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
'''


# use requests module to download content
'''
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
'''


# import beautiful soup 4 (beautify HTML files)
'''
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
'''


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
'''
p_tag = soup.select("p")[0] 
# <p class="cart-block-items collapsed uc-cart-empty">There are no products in your shopping cart.</p>

text = p_tag.getText() # 'There are no products in your shopping cart.'

# get values by attribute name
p_tag.get("class") # ['cart-block-items', 'collapsed', 'uc-cart-empty']

# get non-existent attribute
p_tag.get("non-existent") # returns None
'''


# control Chorme with selenium
'''
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


# find elements by selenium
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

print(element.tag_name)                 # print input
print(element.get_attribute("class"))   # print values of class
print(element.is_displayed())           # print True
print(element.location)                 # its position: {'x': 298, 'y': 324}
# help(webdriver.remote.webelement.WebElement)

browser.quit()
'''


# click a button with selenium
'''

from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://inventwithpython.com")
link_element = browser.find_element_by_link_text("Read It Online")
time.sleep(5)
# click the link
link_element.click()
browser.quit()
'''


# filling out a form
'''
from selenium import webdriver
import time

# open Chrome and go to Google
browser = webdriver.Chrome()
browser.get("https://accounts.google.com/signin/v2")

# enter username
email_element = browser.find_element_by_id("identifierId")
email_element.send_keys("test.cefi@gmail.com")

# submit username
next_element = browser.find_element_by_id("identifierNext")
next_element.click()

# wait for HTML content changes
time.sleep(2)
# enter password
password_element = browser.find_element_by_name("password")
password_element.send_keys("password here")

# submit password
password_next_element = browser.find_element_by_id("passwordNext")
password_next_element.click()
'''


# special keys: arrow, enter, etc
'''
from selenium.webdriver.common.keys import Keys
# keys.DOWN
# keys.UP
# keys.LEFT
# keys.RIGHT

# keys.ENTER
# keys.ESCAPE

# keys.F1
# keys.F5
# keys.TAB

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
time.sleep(1)
htmlElem.send_keys(Keys.END)     # scrolls to bottom
time.sleep(1)
htmlElem.send_keys(Keys.HOME)    # scrolls to top
time.sleep(1)
browser.quit()
'''


# browser buttons
'''
browser.back()
browser.forward()
browser.refresh()
browser.quit()
'''
# more on selenium: http://selenium-python.readthedocs.io/


# process CSV files
'''
import csv
file_handle = open('dummy.csv')
csv_reader = csv.reader(file_handle)
file_content = list(csv_reader)
'''


# datetime and time module
'''
import datetime, time

# returns datetime(year, month, day, hour, minute, second, microsecond
current = datetime.datetime.now()

# 1000 seconds from unix epoch time easter time: December 31, 1969, 19:00
thousand_seconds = datetime.datetime.fromtimestamp(1000)

# get current time using time module
current_from_time = datetime.datetime.fromtimestamp(time.time())

# get time duration
duration = datetime.timedelta(days=11, hours=10, minutes=9, seconds=0)
print(duration.days)            # print 11
print(duration.total_seconds()) # print 986948, total seconds in this duration
print(str(duration))            # print '11 days, 10:09:00'

# get timestamp for 2 days later
two_days = datetime.timedelta(days=2)
two_days_later = current + two_days

# run program at a specific time
desire_time = datetime.datetime(2017, 7, 14, 11, 47, 0)
while datetime.datetime.now() < desire_time:
    # check above condition once every second, reduce busy loop
    time.sleep(1)
print(str(desire_time))

# format string representation of datetime object
yyyy_mm_dd = current.strftime("%Y-%m-%d")

# parse a string to datetime object
parsed = datetime.datetime.strptime("July 1, 2017", "%B %d, %Y")

# wildcards of datetime object
# %Y - year                  e.g. 2017
# %y - year without century  e.g. 17
# %m - month as number       e.g. 01
# %B - month name            e.g. January
# %b - abbreviated month     e.g. Jan
# %d - day of month          e.g. 01 - 31
# %j - day of year           e.g. 01 - 366
# %w - day of week           e.g. 0 - Sunday, 1 - Monday
# %A - full name above       e.g. Monday
# %a - abbreviated name      e.g. Mon
# %H - hour(24)              e.g. 00 - 23
# %I - hour(120              e.g. 01 - 12
# %M - minute                e.g. 00 - 59
# %S - second                e.g. 00 - 59
# %p - am or pm
'''
