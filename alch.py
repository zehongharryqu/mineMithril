import pyautogui
import time

# tuning - sell
BIN_FIRST_POT_X = 575
BIN_FIRST_POT_Y = 525
NEXT_SLOT = 36
PRICE_X = 720
PRICE_Y = 390
ONE_HOUR = True
PRICE = '59999'


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


def shift_click():
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')


if __name__ == '__main__':
    # brew_pots()
    sell_pots()
    