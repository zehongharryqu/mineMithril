"""combines a full inventory of books"""

import pyautogui
import time
import platform


def combine():
    time.sleep(2)
    pyautogui.moveRel(1, 0)
    books_in = 0
    # stage 1
    for i in range(4):
        for j in range(9):
            if i == 3 and j == 7:
                break
            time.sleep(0.5)
            pyautogui.moveTo(first_inv[0] + cell_size * j, first_inv[1] + cell_size * i)
            shift_click()
            books_in += 1
            if books_in == 2:
                pyautogui.moveTo(anvil_top[0], anvil_top[1] + cell_size)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
                books_in = 0
    # stage 2
    for i in range(4):
        for j in range(9):
            if i == 1 and j > 3:
                continue
            if i == 2:
                continue
            if i == 3 and j == 3:
                break
            time.sleep(0.5)
            pyautogui.moveTo(first_inv[0] + cell_size * j, first_inv[1] + cell_size * i)
            shift_click()
            books_in += 1
            if books_in == 2:
                pyautogui.moveTo(anvil_top[0], anvil_top[1] + cell_size)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
                books_in = 0
    # stage 3
    for x in [(0, 0), (0, 1), (0, 2), (3, 0), (3, 1), (3, 4), (3, 5), (3, 6)]:
        time.sleep(0.5)
        pyautogui.moveTo(first_inv[0] + cell_size * x[1], first_inv[1] + cell_size * x[0])
        shift_click()
        books_in += 1
        if books_in == 2:
            pyautogui.moveTo(anvil_top[0], anvil_top[1] + cell_size)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.click()
            books_in = 0
    # stage 4
    for j in range(5):
        if j == 3:
            continue
        time.sleep(0.5)
        pyautogui.moveTo(first_inv[0] + cell_size * j, first_inv[1] + cell_size * 3)
        shift_click()
        books_in += 1
        if books_in == 2:
            pyautogui.moveTo(anvil_top[0], anvil_top[1] + cell_size)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.click()
            books_in = 0


def shift_click():
    pyautogui.keyDown('shift')
    time.sleep(0.25)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.keyUp('shift')


if __name__ == '__main__':
    if platform.system() == "Darwin":
        first_inv = (577, 522)
        anvil_top = (720, 316)
        cell_size = 36
    elif pyautogui.size() == (1366, 768):
        first_inv = (538, 446)
        brew_top = (682, 241)
        cell_size = 36
    else:
        first_inv = (577, 522)
        anvil_top = (720, 316)
        cell_size = 36
    combine()
