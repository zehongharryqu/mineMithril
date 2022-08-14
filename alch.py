import pyautogui
import time
import platform
import sys


def brew_pots():
    time.sleep(2)
    pyautogui.moveRel(1, 0)
    bottles_in = 0
    for i in range(4):
        for j in range(9):
            if i == 3 and j == 6:
                return
            pyautogui.moveTo(first_inv[0] + cell_size * j, first_inv[1] + cell_size * i)
            shift_click()
            bottles_in += 1
            if bottles_in == 3:
                pyautogui.moveTo(first_inv[0] + cell_size * 6, first_inv[1] + cell_size * 3)  # add wart
                shift_click()
                time.sleep(25)
                pyautogui.moveTo(*brew_top)  # remove wart
                shift_click()
                pyautogui.moveTo(first_inv[0] + cell_size * 7, first_inv[1] + cell_size * 3)  # add sugar
                shift_click()
                time.sleep(25)
                pyautogui.moveTo(*brew_top)  # remove sugar
                shift_click()
                for k in range(3):
                    pyautogui.moveTo(brew_top[0] + cell_size * (-2 + 2 * k), brew_top[1] + cell_size * 3)  # pot
                    shift_click()
                bottles_in = 0


def sell_pots():
    time.sleep(2)
    pyautogui.write('e9', interval=0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(brew_top[0], brew_top[1]+cell_size)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    for i in range(4):
        for j in range(9):
            if i == 3 and j == 6:
                return
            pyautogui.click(first_inv[0] + cell_size * j, first_inv[1] + cell_size * i)
            time.sleep(0.5)


def shift_click():
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')


if __name__ == '__main__':
    if platform.system() == "Darwin":
        first_inv = (577, 522)
        brew_top = (720, 316)
        cell_size = 36
    elif pyautogui.size() == (1366, 768):
        first_inv = (538, 446)
        brew_top = (682, 241)
        cell_size = 36
    else:
        first_inv = (577, 522)
        brew_top = (720, 316)
        cell_size = 36
    brew_pots()
    sell_pots()
