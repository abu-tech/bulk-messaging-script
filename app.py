import pyautogui as gui
import time

message = input("Enter Message : ")
number= input("Enter Number : ")

time.sleep(2)

for i in range(int(number)) :
    gui.typewrite(message)
    time.sleep(1)
    gui.press('Enter')