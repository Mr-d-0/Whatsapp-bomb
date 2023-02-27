import pywhatkit
import pyfiglet
import pyautogui
import time
ascii_banner = pyfiglet.figlet_format("Mr-D")
print(ascii_banner)
time.sleep(4)
count=0
while count<=10:
    pyautogui.typewrite("U R H4CKED")
    pyautogui.press("enter")
    count=count+1