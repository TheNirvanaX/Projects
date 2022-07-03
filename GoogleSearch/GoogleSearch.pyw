# GoogleSearch -> this program searches clipboard copied text in the GOOGLE.

import re
import sys
import time
import webbrowser

import keyboard
import pyautogui
import pyperclip


def autoCopy():  # copying using virtual keypress

    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    time.sleep(0.1)
    pyautogui.keyUp("ctrl")
    return pyperclip.paste()


def urlSe(text):  # detect url adress pattern

    urlRegex = re.compile(r"(https://)?(www.)?\w+\.[a-zA-Z]{2,4}")
    mo = urlRegex.search(text)
    if mo is None:
        text = "www.google.com/search?q=" + text  # google search url
    if "https://" not in text:
        text = "https://" + text  # adding https://
    return text


while True:
    try:
        if keyboard.is_pressed("g + s"):  # trigger for copying and search
            if len(sys.argv) > 1:  # if search is made from run or CLI
                text = " ".join(sys.argv[1:])
            else:
                text = autoCopy()  # get text from clipboard
            searchterm = urlSe(text)  # search url for google
            webbrowser.open(searchterm)

        if keyboard.is_pressed("q + t"):  # stop program
            sys.exit()

    except KeyboardInterrupt:  # ctrl+c interrupt
        sys.exit()
