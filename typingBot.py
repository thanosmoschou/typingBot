"""
Author: Thanos Moschou
Description: 
This is a speed typing bot. It uses pyautogui and easyocr modules.
First it takes a screenshot of a specified area that contains text. Then it uses easyocr module for optical character recognition. 
Finally it writes the recognized text to the website's
specified area.
Site: https://10fastfingers.com/typing-test/english
It repeats the process for 60 seconds.
Disclaimers: You have to prepare the website yourself before you run the script. 
Go to the page and click "Start typing test". Make sure the active window is the browser's window.
Also due to the fact that it uses ocr methods, it is pretty inconsistent.
The coordinates are for 15 inch screens.

It is made for educational purposes only.
Use it at your own risk.

Last modification date: 26/11/2023
"""

import pyautogui
import time
import easyocr
from PIL import Image

positionScreenshotX = 325
positionScreenshotY = 344
positionMouseX = 545
positionMouseY = 531
imageWidth = 1180
imageHeight = 136

reader = easyocr.Reader(["en"])
pyautogui.click(positionMouseX, positionMouseY) #click on the text field that will be filled 
imageName = "words.png"

currTime = 0

while currTime < 30: #this will run for 60 seconds. Screenshot and read text take about 2 seconds.
    pyautogui.screenshot(imageName, region=(positionScreenshotX, positionScreenshotY, imageWidth, imageHeight))
    results = reader.readtext(imageName)

    for tup in results:
        pyautogui.write(tup[1]) #2nd element of each tupple has the string I want
        pyautogui.press("space")
    
    currTime += 1
