import pyautogui
import cv2
import keyboard
import sys
import time
from PIL import ImageGrab
import win32api,win32con


#time.sleep(5)
# Jump position -> X:  361 Y:  688
# cactus rgb -> RGB: (172, 172, 172)
def hit():
#    win32api.keybd_event(0x20, 0, 0, 0)
#    win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_KEYUP, 0)
    pyautogui.press("space")

#def autoScreenshot():
#   img = ImageGrab.grab()
#s   return img

def play():
    while True:
        if pyautogui.pixelMatchesColor(410, 688, (172,172,172),tolerance=10) or pyautogui.pixelMatchesColor(310, 688, (172,172,172),tolerance=10):
            hit()
            print("yes")

#        if keyboard.e == "esc":
#          sys.exit()
#        print("no")
#        time.sleep(0.05)
while True:
    try:
        if keyboard.read_key() == "s":
            play()
    except KeyboardInterrupt:
        sys.exit()