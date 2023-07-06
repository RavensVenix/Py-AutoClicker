import pyautogui as py
from lib.click import click

def check_password(password):
    if password == "PianoTiles":
        print("Password Correct!")
    else:
        print("Password Incorrect!")
        
