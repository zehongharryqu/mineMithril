from PIL import ImageGrab
import pyautogui
import time
import keyboard


def centered_box(width):
    screen_size = pyautogui.size()
    return [screen_size[0] - width, screen_size[1] - width, screen_size[0] + width, screen_size[1] + width]


def mine():
    # switch windows
    time.sleep(3)
    # state vars
    mouse_down = False
    pixels_moved = 0
    num_fails = 0
    view_box_coords = centered_box(10)
    started_mining_time = time.perf_counter()
    loop_count = 0
    # lets begin!
    pyautogui.moveRel(1, 0)
    while True:
        if keyboard.is_pressed("e"):
            break
        if num_fails == 5:
            break
        im = ImageGrab.grab(bbox=view_box_coords)
        rgb_im = im.convert('RGB')
        should_be_mining = not looking_at_bedrock(rgb_im)
        if (not mouse_down) and should_be_mining:
            pyautogui.mouseDown()
            mouse_down = True
            started_mining_time = time.perf_counter()
        elif mouse_down and (not should_be_mining):
            pyautogui.mouseUp()
            mouse_down = False
        elif (not mouse_down) and (not should_be_mining):
            pixels_moved = next_block(pixels_moved)
            num_fails = 0
        else:
            time_mined = time.perf_counter() - started_mining_time
            if time_mined > 3:
                pyautogui.mouseUp()
                mouse_down = False
                pixels_moved = next_block(pixels_moved)
                num_fails += 1
        # randomly move?
        if loop_count == 1:
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('d')
        elif loop_count == 3:
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('d')
        elif loop_count == 6:
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('a')
        elif loop_count == 8:
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('a')
        elif loop_count == 10:
            loop_count = 0
        loop_count += 1

    pyautogui.keyUp('ctrl')
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.click(690, 540)


def looking_at_bedrock(pixel_array):
    threshold = 10
    for i in range(20):
        for j in range(20):
            r, g, b = pixel_array.getpixel((i, j))
            if (r < threshold) and (g < threshold) and (b < threshold):
                return True
    return False


def next_block(pixels_moved):
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
    mine()
