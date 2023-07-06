import pyautogui as py
import time
import keyboard
import random
import win32api
import win32con
from lib.checkPassword import check_password
from lib.password import pwsd
from lib.noText import no_text
from lib.click import click

# Perulangan untuk terus meminta password
running = True
while running:
    password = pwsd()
    if password is None:
        print("Canceled!")
        print("Script ended.")
        break
    elif password == '':
        while True:
            password = no_text()
            if password is None:
                print("Canceled!")
                print("Script ended.")
                break
            elif password != '':
                break

    if password is None:
        print("Canceled!")
        print("Script ended.")
        break

    confirm = py.confirm(text="Password: " + password, title='Confirm Password', buttons=['OK', 'Cancel'])
    if confirm == 'OK':
        check_password(password)

    if password == 'PianoTiles':
        while True:
            if keyboard.is_pressed('q'):
                running = False
                break

            if py.pixel(647, 370):
                click(647, 370)
