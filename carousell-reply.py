# This script automates replying to all interested customers on Carousell
# Adapt code according to any Carousell UI changes

# pip install selenium
# brew install chromedriver (for OS X only, windows can try https://chromedriver.storage.googleapis.com/index.html?path=2.26/)
# pip install splinter

from splinter import Browser
import time

with Browser('chrome') as browser:

    # Visit Carousell and login
    mainurl = "https://sg.carousell.com/inbox/"
    browser.visit(mainurl)
    browser.fill('username', 'USERNAME') # replace with own username and password
    browser.fill('pass', 'PASSWORD')
    buttonLogin = browser.find_by_text("Log in")
    buttonLogin.click()
    time.sleep(3) # Loading buffer

    # Store and visit all available chats
    invalidLinks = ['https://sg.carousell.com/inbox/','https://sg.carousell.com/inbox/?q=buying', 'https://sg.carousell.com/inbox/?q=selling']
    chatsFound = browser.find_link_by_partial_href('inbox')
    chatLinks = []
    for chat in chatsFound:
        if chat['href'] not in invalidLinks:
            chatLinks.append(chat['href'])

    for chatLink in chatLinks:
        browser.visit(chatLink)

        # (1) Send message
        messageBox = browser.find_by_tag('textarea')
        messageBox.fill('hey') # change to the correct message
        time.sleep(2)
        sendBtn = browser.find_by_text('Send')
        sendBtn.click()
        time.sleep(2)

        # (2) Archive message to prevent duplicates in next script run
        textPath = browser.find_by_xpath("//span[.='Archive']")
        browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        textPath.click()
        time.sleep(1)


    # Remove above (2) and use code below for mass archiving
    # (faster, but might auto archive chats that are just created in duration of script run)
    # browser.visit(mainurl)
    # browser.find_by_value('on').first.check()
    # time.sleep(1)
    # browser.find_by_text('Archive').click()
    # time.sleep(3)
