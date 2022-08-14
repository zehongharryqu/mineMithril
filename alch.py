import pyautogui
import time

# Mac
# FIRST_INV = (577, 522)
# BREW_TOP = (720, 316)
FIRST_INV = (577, 522)
BREW_TOP = (720, 316)
NEXT_SLOT = 36


def brew_pots():
    time.sleep(2)
    pyautogui.moveRel(1, 0)
    bottles_in = 0
    for i in range(4):
        for j in range(9):
            if i == 3 and j == 6:
                return
            pyautogui.moveTo(FIRST_INV[0] + NEXT_SLOT * j, FIRST_INV[1] + NEXT_SLOT * i)
            shift_click()
            bottles_in += 1
            if bottles_in == 3:
                pyautogui.moveTo(FIRST_INV[0] + NEXT_SLOT * 6, FIRST_INV[1] + NEXT_SLOT * 3)  # add wart
                shift_click()
                time.sleep(22)
                pyautogui.moveTo(*BREW_TOP)  # remove wart
                shift_click()
                pyautogui.moveTo(FIRST_INV[0] + NEXT_SLOT * 7, FIRST_INV[1] + NEXT_SLOT * 3)  # add sugar
                shift_click()
                time.sleep(22)
                pyautogui.moveTo(*BREW_TOP)  # remove sugar
                shift_click()
                for k in range(3):
                    pyautogui.moveTo(BREW_TOP[0] + NEXT_SLOT * (-2 + 2 * k), BREW_TOP[1] + NEXT_SLOT * 3)  # pot
                    shift_click()
                bottles_in = 0


def sell_pots():
    time.sleep(2)
    pyautogui.write('e9', interval=0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(BREW_TOP[0], BREW_TOP[1]+NEXT_SLOT)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    for i in range(4):
        for j in range(9):
            if i == 3 and j == 6:
                return
            pyautogui.click(FIRST_INV[0] + NEXT_SLOT * j, FIRST_INV[1] + NEXT_SLOT * i)
            time.sleep(0.5)


def shift_click():
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')


if __name__ == '__main__':
    brew_pots()
    sell_pots()
