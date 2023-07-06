## Py-AutoClicker
Py-AutoClicker is a bot that uses Python language which functions to automate mouse clicks for applications or websites that rely on mouse clicks such as popcat.click, popdog.click 
- *Just for fun only!*

## Screenshots :
- [PopDog.click](https://popdog.click/)
<img src="https://i.postimg.cc/bwv1hch5/Capture.png">

- [PopCat.click](https://popcat.click/)
<img src="https://i.postimg.cc/vmkKnthQ/Capture.png">

## Requirements :
- [Python](https://python.org/)
- [Git](https://git-scm.com/downloads)

## Used Lib :
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/install.html)

## Install PyAutoGUI :
- For Windows
```bash
pip install pyautogui
```
- For macOS and Linux
```bash
pip3 install pyautogui
```

## Change mouse position :
- Open Python IDLE Shell
```python
>>> import pyautogui
>>> pyautogui.displayMousePosition()
```
- You will get the mouse position according to your mouse pointer, if you want to point it at an image to click then point your mouse pointer at the image then wait 1 second after that return to the Python IDLE Shell earlier, Position example :
```
Press Ctrl-C to quit.
X:  757 Y:  363 RGB: (255, 255, 255)
X:  722 Y:  135 RGB: ( 76,  76,  76)
```
- Copy the X and Y Position then go [*here*](https://github.com/RavensVenix/Py-AutoClicker/blob/70529253a4c28e21ed8caa50c622afbce1b0488e/main.py#L45) then change 647, 370 to the mouse position you copied earlier.

## Command Line :
```bash
git clone https://github.com/RavensVenix/Py-AutoClicker.git
cd Py-AutoClicker
python3 main.py / python main.py
```

## Run it :
- Password is :
```
Py-AutoClick
```
*You can change the password* [*here*](https://github.com/RavensVenix/Py-AutoClicker/blob/9f7d56353d0866629a28ab5af61cfafb163a409e/lib/checkPassword.py#L5C35-L5C35)

- Next step
<p>Don't confirm the password, first go to the application or website you want to go to.<br>
then if you have confirmed the password then the script will run

## How to stop?
- To stop :
```
Press Q on your keyboard.
```
*You can change it* [*here*](https://github.com/RavensVenix/Py-AutoClicker/blob/9f7d56353d0866629a28ab5af61cfafb163a409e/main.py#L41)
