from PIL import ImageGrab
import pyautogui
import time

# screen centre 683, 384
viewBoxCoordsLeft = [608, 334, 658, 434]
viewBoxCoordsRight = [708, 334, 758, 434]
MITHR = 27
MITHG = 75
MITHB = 76
threshold = 30


def minemithril():
    time.sleep(3)
    mouse_down = False
    pixels_moved = 0
    # pyautogui.moveTo(100, 150)
    pyautogui.moveRel(10, 0)
    while True:
        left_box = ImageGrab.grab(bbox=viewBoxCoordsLeft)
        right_box = ImageGrab.grab(bbox=viewBoxCoordsRight)
        main_colours_left = left_box.quantize(colors=2, method=2)
        main_colours_right = right_box.quantize(colors=2, method=2)
        main_col_left_1 = main_colours_left.getpalette()[:3]
        main_col_left_2 = main_colours_left.getpalette()[3:6]
        main_col_right_1 = main_colours_right.getpalette()[:3]
        main_col_right_2 = main_colours_right.getpalette()[3:6]
        main_col_left_1_mith = (abs(main_col_left_1[0] - MITHR) < threshold) and \
                               (abs(main_col_left_1[1] - MITHG) < threshold) and \
                               (abs(main_col_left_1[2] - MITHB) < threshold)
        main_col_right_1_mith = (abs(main_col_right_1[0] - MITHR) < threshold) and \
                                (abs(main_col_right_1[1] - MITHG) < threshold) and \
                                (abs(main_col_right_1[2] - MITHB) < threshold)
        main_col_left_2_mith = (abs(main_col_left_2[0] - MITHR) < threshold) and \
                               (abs(main_col_left_2[1] - MITHG) < threshold) and \
                               (abs(main_col_left_2[2] - MITHB) < threshold)
        main_col_right_2_mith = (abs(main_col_right_2[0] - MITHR) < threshold) and \
                                (abs(main_col_right_2[1] - MITHG) < threshold) and \
                                (abs(main_col_right_2[2] - MITHB) < threshold)
        should_be_mining = (main_col_left_1_mith or main_col_left_2_mith) \
                           and (main_col_right_1_mith or main_col_right_2_mith)
        if (not mouse_down) and should_be_mining:
            pyautogui.mouseDown()
            mouse_down = True
            started_mining_time = time.perf_counter()
        elif mouse_down and (not should_be_mining):
            pyautogui.mouseUp()
            mouse_down = False
        elif (not mouse_down) and (not should_be_mining):
            if pixels_moved < 300:
                pyautogui.moveRel(10, 0)
                pixels_moved += 10
            elif pixels_moved < 400:
                pyautogui.moveRel(0, 10)
                pixels_moved += 10
            elif pixels_moved < 700:
                pyautogui.moveRel(-10, 0)
                pixels_moved += 10
            elif pixels_moved < 1000:
                pyautogui.moveRel(0, -10)
                pixels_moved += 10
            else:
                break
        else:
            time_mined = time.perf_counter() - started_mining_time
            if time_mined > 5000:
                pyautogui.mouseUp()
                mouse_down = False
                pyautogui.moveRel(100, 0)


if __name__ == '__main__':
    minemithril()
