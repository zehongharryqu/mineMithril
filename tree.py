from PIL import ImageGrab
import pyautogui
import time

# coords of screen centre in px, starting at topleft
SCREENCENTREX = 683
SCREENCENTREY = 384

# coords of item details
ITEMDETAILSX = 302
ITEMDETAILSY = 665


def chop_tree():
    time.sleep(3)
    mouse_down = False
    w_down = False
    stopped_time = time.perf_counter()
    pyautogui.moveRel(1, 0)
    while True:
        should_be_chopping = red_box(ITEMDETAILSX, ITEMDETAILSY, 1, 1, True)
        if should_be_chopping:
            if w_down:
                pyautogui.keyUp('w')
                w_down = False
                stopped_time = time.perf_counter()
            else:
                time_stopped = time.perf_counter() - stopped_time
                if time_stopped > 2:
                    pyautogui.moveRel(1000, 0)
            if not mouse_down:
                pyautogui.mouseDown()
                mouse_down = True
                started_chopping_time = time.perf_counter()
            else:
                time_mined = time.perf_counter() - started_chopping_time
                if time_mined > 1:
                    pyautogui.mouseUp()
                    mouse_down = False
                    pyautogui.moveRel(1000, 0)
        else:
            if mouse_down:
                pyautogui.mouseUp()
                mouse_down = False
            else:
                tree_in_sight = red_box(SCREENCENTREX - 25, SCREENCENTREY - 200, 50, 300, False)
                if tree_in_sight:
                    if not w_down:
                        pyautogui.keyDown('w')
                        w_down = True
                        started_moving_time = time.perf_counter()
                    else:
                        time_moved = time.perf_counter() - started_moving_time
                        if time_moved > 5:
                            pyautogui.keyUp('w')
                            w_down = False
                            pyautogui.keyDown('s')
                            time.sleep(0.5)
                            pyautogui.keyUp('s')
                            pyautogui.moveRel(100, 0)
                else:
                    if w_down:
                        pyautogui.keyUp('w')
                        w_down = False
                        stopped_time = time.perf_counter()
                    else:
                        time_stopped = time.perf_counter() - stopped_time
                        if time_stopped > 2:
                            pyautogui.moveRel(1000, 0)
                    next_tree = red_box(0, SCREENCENTREY - 100, 2 * SCREENCENTREX, 200, False)
                    if next_tree:
                        look_dist = (next_tree[0] - SCREENCENTREX)/1.4
                        if look_dist > 0:
                            pyautogui.moveRel(look_dist + 25, 0)
                        else:
                            pyautogui.moveRel(look_dist - 25, 0)
                    else:
                        pyautogui.moveRel(500, 0)


# (x,y) is top left. determines if it is all red/contains red
def red_box(x, y, width, height, all_required):
    viewbox = [x, y, x + width, y + height]
    im = ImageGrab.grab(bbox=viewbox)
    im.save("testimg.png")
    rgb_im = im.convert('RGB')
    for i in range(width):
        for j in range(height):
            r, g, b = rgb_im.getpixel((i, j))
            if all_required and not ((r > 150) and (g < 10) and (b < 10)):
                return []
            if not all_required and ((r > 150) and (g < 10) and (b < 10)):
                return [x + i, y + j]
    if all_required:
        return [x, y]
    else:
        return []


if __name__ == '__main__':
    chop_tree()
