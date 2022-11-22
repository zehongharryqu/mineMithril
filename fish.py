"""fish"""

from PIL import ImageGrab
from pynput.mouse import Button, Controller
import time

mouse = Controller()


def fish():
    time.sleep(2)
    while True:
        time.sleep(1)
        mouse.click(Button.right, 1)
        time.sleep(3)
        while True:
            if see_fish():
                mouse.click(Button.right, 1)
                break


def see_fish():
    im = ImageGrab.grab(bbox=(1000, 400, 1800, 1200))
    for i in range(80):
        for j in range(80):
            rgb = im.getpixel((i*10, j*10))
            if rgb[0] > 190 and rgb[1] < 50:
                return True
    return False


if __name__ == '__main__':
    fish()
