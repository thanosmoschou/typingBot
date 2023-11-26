## Typing Bot
This is a simple speed typing bot built with Python. <br>
It uses easyocr and pyautogui modules of Python. <br>

### How it works
This works for the following site: <br>
```https://10fastfingers.com/typing-test/english``` <br>
Keep in mind that if you change some coordinates, it can work for different sites also.

First it takes a screenshot of a specified area that contains some text.  <br>
Then it uses OCR methods to recognize the text. <br>
Finally, it writes the text to the specified area within the website. <br>
It repeats the process for 60 seconds.

### How to run it
Make sure you have python installed on your pc. <br>
Open the project's folder in a terminal. <br>
Type:
```
pip install -r requirements.txt
```
and then: <br>
```
python typingBot.py
```

### Disclaimers
You have to prepare the website yourself before you run the script. <br>
Go to the page and click ```Start typing test```. <br>
Make sure the active window is the browser's window. <br>
Also due to the fact that it uses OCR methods, it is pretty inconsistent. <br>
The coordinates are tested for 15 inch screens. <br><br>
This script is made for educational purposes only. <br>
It is made to show how you can scrape text from images. <br>
Use it at your own risk. <br>
Author is not responsible for any damage you may cause by using this script. <br>
