from PIL import ImageGrab
import pyautogui
import time
import keyboard

# tuning
STEP_SIZE = 50
WIDTH_STEPS = 10
HEIGHT_STEPS = 2
DC_X = 690
DC_Y = 540


def centered_box(width):
    screen_size = pyautogui.size()
    centre_x = screen_size[0] / 2
    centre_y = screen_size[1] / 2
    return [centre_x - width, centre_y - width, centre_x + width, centre_y + width]


def mine():
    # switch windows
    time.sleep(3)
    # state vars
    mouse_down = False
    steps_moved = 0
    num_fails = 0
    view_box_coords = centered_box(10)
    loop_count = 0
    started_mining_time = time.perf_counter()
    # lets begin!
    pyautogui.moveRel(1, 0)
    try:
        while True:
            if keyboard.is_pressed("e"):
                break
            assert (num_fails < 5), "too many failed blocks"
            im = ImageGrab.grab(bbox=view_box_coords)
            rgb_im = im.convert('RGB')
            should_be_mining = not looking_at_bedrock(rgb_im, 20)
            if (not mouse_down) and should_be_mining:
                pyautogui.mouseDown()
                mouse_down = True
                started_mining_time = time.perf_counter()
            elif mouse_down and (not should_be_mining):
                pyautogui.mouseUp()
                mouse_down = False
            elif (not mouse_down) and (not should_be_mining):
                steps_moved = next_block(steps_moved)
                num_fails = 0
            else:
                time_mined = time.perf_counter() - started_mining_time
                if time_mined > 5:
                    pyautogui.mouseUp()
                    mouse_down = False
                    steps_moved = next_block(steps_moved)
                    num_fails += 1
            # move back and forth
            # if loop_count == 1:
            #     pyautogui.keyDown('ctrl')
            #     pyautogui.keyDown('d')
            # elif loop_count == 2:
            #     pyautogui.keyUp('ctrl')
            #     pyautogui.keyUp('d')
            # elif loop_count == 11:
            #     pyautogui.keyDown('ctrl')
            #     pyautogui.keyDown('a')
            # elif loop_count == 12:
            #     pyautogui.keyUp('ctrl')
            #     pyautogui.keyUp('a')
            # elif loop_count == 20:
            #     loop_count = 0
            # loop_count += 1
    except Exception as e:
        print(e)
        pyautogui.keyUp('ctrl')
        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.click(DC_X, DC_Y)


def looking_at_bedrock(pixel_array, width):
    threshold = 10
    for i in range(width):
        for j in range(width):
            r, g, b = pixel_array.getpixel((i, j))
            if (r < threshold) and (g < threshold) and (b < threshold):
                return True
    return False


def next_block(steps_moved):
    if steps_moved < WIDTH_STEPS:
        pyautogui.moveRel(STEP_SIZE, 0)
        steps_moved += 1
    elif steps_moved < WIDTH_STEPS + HEIGHT_STEPS:
        pyautogui.moveRel(0, STEP_SIZE)
        steps_moved += 1
    elif steps_moved < 2 * WIDTH_STEPS + HEIGHT_STEPS:
        pyautogui.moveRel(-STEP_SIZE, 0)
        steps_moved += 1
    elif steps_moved < 2 * WIDTH_STEPS + 2 * HEIGHT_STEPS:
        pyautogui.moveRel(0, STEP_SIZE)
        steps_moved += 1
    elif steps_moved < 3 * WIDTH_STEPS + 2 * HEIGHT_STEPS:
        pyautogui.moveRel(STEP_SIZE, 0)
        steps_moved += 1
    elif steps_moved < 3 * WIDTH_STEPS + 3 * HEIGHT_STEPS:
        pyautogui.moveRel(0, STEP_SIZE)
        steps_moved += 1
    elif steps_moved < 4 * WIDTH_STEPS + 3 * HEIGHT_STEPS:
        pyautogui.moveRel(-STEP_SIZE, 0)
        steps_moved += 1
    else:
        pyautogui.moveRel(0, -STEP_SIZE * HEIGHT_STEPS * 3)
        steps_moved = 0
    return steps_moved


if __name__ == '__main__':
    mine()
