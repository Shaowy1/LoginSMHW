import time
import constants
import pyautogui
import os
import multiprocessing
import subprocess
import keyboard
import mouse

def prevent_input(duration):
    keyboard_process = multiprocessing.Process(target=prevent_keyboard)
    mouse_process = multiprocessing.Process(target=prevent_mouse)
    keyboard_process.start()
    mouse_process.start()
    time.sleep(duration)
    keyboard_process.close()
    mouse_process.close()

def prevent_keyboard():
    for i in range(150):
        keyboard.block_key(i)

def prevent_mouse():
    while True:
        mouse.move(1, 0, absolute=True, duration=0)

def login():
    subprocess.call(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(0.5)
    pyautogui.click(constants.PROFILE[0], constants.PROFILE[1])
    time.sleep(1)
    pyautogui.click(constants.GUEST[0], constants.GUEST[1])
    pyautogui.typewrite('https://www.satchelone.com/login')
    pyautogui.press('enter')

login()