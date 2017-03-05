# This script automates replying to all interested customers on GumTree
# Adapt code according to any GumTree UI changes

# pip install selenium
# brew install chromedriver (for OS X only, windows can try https://chromedriver.storage.googleapis.com/index.html?path=2.26/)
# pip install splinter

from splinter import Browser
import time

with Browser('chrome') as browser:

    # Visit Carousell and login
    mainurl = "https://www.gumtree.sg/my/message.html"
    browser.visit(mainurl)
    browser.fill('email', 'primedeliveryenquiry@gmail.com') # replace with own username and password
    browser.fill('password', 'somepw')
    buttonLogin = browser.find_by_text("Log in")
    buttonLogin.click()
    time.sleep(1) # Loading buffer

    while (browser.is_element_present_by_css('.conv-mc')):
        chat = browser.find_by_css('.conv-mc').first
        chat.click()
        time.sleep(1)
        messageBox = browser.find_by_tag('textarea')
        messageBox.fill('hey') # change to the correct message
        time.sleep(1)
        sendBtn = browser.find_by_text('Send')
        sendBtn.click()
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        browser.find_by_css('.backToConv').click()
        time.sleep(1)
        browser.find_by_css('.icon-delete').click()
        browser.find_by_css('.Yes').click()
        time.sleep(1)
    time.sleep(1)
