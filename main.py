import pyautogui
import time
import keyboard
import os
import platform

# tuning
STEP_SIZE = 50
WIDTH_STEPS = 5
HEIGHT_STEPS = 1
DC_X = 690
DC_Y = 540


def mine():
    # switch windows
    time.sleep(3)
    # state vars
    mouse_down = False
    steps_moved = 0
    num_fails = 0
    loop_count = 0
    started_mining_time = time.perf_counter()
    # lets begin!
    move_rel(1, 0)
    try:
        while True:
            # if keyboard.is_pressed("e"):
            #     break
            assert (num_fails < 3), "too many failed blocks"
            should_be_mining = not looking_at_bedrock()
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
                if time_mined > 7:
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


def looking_at_bedrock():
    screen_size = pyautogui.size()
    x = screen_size[0]
    y = screen_size[1]
    return pyautogui.pixelMatchesColor(x, y, (0, 1, 0))


def next_block(steps_moved):
    if steps_moved < WIDTH_STEPS:
        move_rel(STEP_SIZE, 0)
        steps_moved += 1
    elif steps_moved < WIDTH_STEPS + HEIGHT_STEPS:
        move_rel(0, STEP_SIZE)
        steps_moved += 1
    elif steps_moved < 2 * WIDTH_STEPS + HEIGHT_STEPS:
        move_rel(-STEP_SIZE, 0)
        steps_moved += 1
    elif steps_moved < 2 * WIDTH_STEPS + 2 * HEIGHT_STEPS:
        move_rel(0, STEP_SIZE)
        steps_moved += 1
    elif steps_moved < 3 * WIDTH_STEPS + 2 * HEIGHT_STEPS:
        move_rel(STEP_SIZE, 0)
        steps_moved += 1
    elif steps_moved < 3 * WIDTH_STEPS + 3 * HEIGHT_STEPS:
        move_rel(0, STEP_SIZE)
        steps_moved += 1
    elif steps_moved < 4 * WIDTH_STEPS + 3 * HEIGHT_STEPS:
        move_rel(-STEP_SIZE, 0)
        steps_moved += 1
    else:
        move_rel(0, -STEP_SIZE * HEIGHT_STEPS * 3)
        steps_moved = 0
    return steps_moved


def move_rel(right, down):
    if platform.system() == "Darwin":
        if right != 0:
            if right > 0:
                keycode = 88
            else:
                right *= -1
                keycode = 86
            cmd = f""" osascript -e '
                        repeat {right*2} times
                            tell application "System Events" to key code {keycode}
                        end repeat'
                    """
            os.system(cmd)
        if down != 0:
            if down > 0:
                keycode = 84
            else:
                down *= -1
                keycode = 91
            cmd = f""" osascript -e '
                        repeat {down*2} times
                            tell application "System Events" to key code {keycode}
                        end repeat'
                    """
            os.system(cmd)
    else:
        pyautogui.moveRel(right, down)


if __name__ == '__main__':
    mine()
