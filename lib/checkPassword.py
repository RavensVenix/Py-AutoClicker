import pyautogui as py
from lib.click import click

def check_password(password):
    if password == "Py-AutoClick":
        print("Password Correct!")
    else:
        print("Password Incorrect!")
        
