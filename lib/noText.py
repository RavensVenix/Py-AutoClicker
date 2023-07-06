import pyautogui as py

def no_text():
    return py.password(text='No password detected! Please enter password :', title='Login first.', default='', mask='*')
	
