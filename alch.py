
import pyautogui
import time


def brew_pots():
    time.sleep(2)
    pyautogui.moveRel(1, 0)
    bottles_in = 0
    for i in range(4):
        for j in range(9):
            if i == 3 and j == 6:
                return
            pyautogui.moveTo(540 + 36 * j, 450 + 36 * i)
            shift_click()
            bottles_in += 1
            if bottles_in == 3:
                pyautogui.moveTo(755, 565)  # wart
                shift_click()
                time.sleep(22)
                pyautogui.moveTo(680, 240)  # top
                shift_click()
                pyautogui.moveTo(755 + 36, 565)  # sugar
                shift_click()
                time.sleep(22)
                pyautogui.moveTo(680, 240)  # top
                shift_click()
                for k in range(3):
                    pyautogui.moveTo(610 + 72 * k, 350)  # pot
                    shift_click()
                bottles_in = 0


def sell_pots():
    time.sleep(2)
    pyautogui.moveRel(1, 0)
    for i in range(4):
        for j in range(9):
            if i == 1 and j == 5:
                return
            pyautogui.moveTo(540 + 36 * j, 445 + 36 * i)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(755, 310)  # duration
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(575, 275)  # 1hr
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(755 - 2 * 36, 310)  # price
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('195', interval=0.25)
            pyautogui.moveTo(680, 460)  # done
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(755 - 4 * 36, 310)  # submit
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(610, 295)  # confirm
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(685, 390)  # go back
            pyautogui.click()
            time.sleep(0.5)


def shift_click():
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')


if __name__ == '__main__':
    # brew_pots()
    sell_pots()