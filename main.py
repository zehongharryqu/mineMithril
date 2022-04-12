from PIL import ImageGrab
import pyautogui
import time

# screen centre 683, 384
viewBoxCoords = [673, 374, 693, 394]

def mineMithril():
    time.sleep(3)
    mouse_down = False
    pixels_moved = 0
    pyautogui.moveRel(1, 0)
    while True:
        im = ImageGrab.grab(bbox=viewBoxCoords)
        rgb_im = im.convert('RGB')
        should_be_mining = not lookingAtBedrock(rgb_im)
        if (not mouse_down) and should_be_mining:
            pyautogui.mouseDown()
            mouse_down = True
            started_mining_time = time.perf_counter()
        elif mouse_down and (not should_be_mining):
            pyautogui.mouseUp()
            mouse_down = False
        elif (not mouse_down) and (not should_be_mining):
            pixels_moved = nextBlock(pixels_moved)
        else:
            time_mined = time.perf_counter() - started_mining_time
            if time_mined > 5:
                pyautogui.mouseUp()
                mouse_down = False
                pixels_moved = nextBlock(pixels_moved)


def lookingAtBedrock(pixelarray):
    threshold = 10
    for i in range(20):
        for j in range(20):
            r, g, b = pixelarray.getpixel((i, j))
            if (r < threshold) and (g < threshold) and (b < threshold):
                return True
    return False


def nextBlock(pixels_moved):
    if pixels_moved < 500:
        pyautogui.moveRel(50, 0)
        pixels_moved += 50
    elif pixels_moved < 600:
        pyautogui.moveRel(0, 50)
        pixels_moved += 50
    elif pixels_moved < 1100:
        pyautogui.moveRel(-50, 0)
        pixels_moved += 50
    elif pixels_moved < 1200:
        pyautogui.moveRel(0, 50)
        pixels_moved += 50
    elif pixels_moved < 1700:
        pyautogui.moveRel(50, 0)
        pixels_moved += 50
    elif pixels_moved < 1800:
        pyautogui.moveRel(0, 50)
        pixels_moved += 50
    elif pixels_moved < 2300:
        pyautogui.moveRel(-50, 0)
        pixels_moved += 50
    else:
        pyautogui.moveRel(0, -300)
        pixels_moved = 0
    return pixels_moved


if __name__ == '__main__':
    mineMithril()
