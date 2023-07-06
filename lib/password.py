import pyautogui as py

def pwsd():
    return py.password(text='Password :', title='Login first.', default='', mask='*')
	
