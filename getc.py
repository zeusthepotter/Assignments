#!C:\Users\Vivek\PycharmProjects\test\venv\Scripts\python.exe

import pyautogui, time
 
while 1:
    x,y=pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    pixelColor = pyautogui.screenshot().getpixel((x, y))
    positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
    positionStr += ', ' + str(pixelColor[1]).rjust(3)
    positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)





