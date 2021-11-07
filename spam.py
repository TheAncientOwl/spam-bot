import pyautogui
import time

time.sleep(8)

f = open("bee-movie-script.txt", "r")

# x used to pause the spam for 3 seconds to avoid discord *enter chill zone*
x = 0
for line in f:
    pyautogui.typewrite(line)
    pyautogui.press("enter")

    x = x + 1
    if x == 10:
        x = 0
        time.sleep(3)
    else:
        time.sleep(0.6)
