import pyautogui
import time
import sys

# tuning
BIN_FIRST_POT_X = 575
BIN_FIRST_POT_Y = 525
NEXT_SLOT = 36
PRICE_X = 720
PRICE_Y = 390


def sell(quantity, price, one_hour):
    time.sleep(2)
    pyautogui.moveRel(1, 0)
    for i in range(4):
        for j in range(9):
            if not quantity:
                return
            pyautogui.moveTo(BIN_FIRST_POT_X + NEXT_SLOT * j, BIN_FIRST_POT_Y + NEXT_SLOT * i)
            pyautogui.click()
            time.sleep(1)
            if one_hour:
                pyautogui.moveTo(PRICE_X + 2 * NEXT_SLOT, PRICE_Y)  # duration
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(PRICE_X - 3 * NEXT_SLOT, PRICE_Y - NEXT_SLOT)  # 1hr
                pyautogui.click()
                time.sleep(1)
            pyautogui.moveTo(PRICE_X, PRICE_Y)  # price
            pyautogui.click()
            time.sleep(1)
            pyautogui.write(str(price), interval=0.25)
            pyautogui.moveTo(725, 485)  # done
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(PRICE_X - 2 * NEXT_SLOT, PRICE_Y)  # submit
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(PRICE_X - 2 * NEXT_SLOT, PRICE_Y - NEXT_SLOT / 2)  # confirm
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(PRICE_X, PRICE_Y + 2 * NEXT_SLOT)  # go back
            pyautogui.click()
            time.sleep(1)
            quantity -= 1


if __name__ == '__main__':
    args = sys.argv[1:]
    try:
        if len(args) != 3:
            raise ValueError
        args = [int(x) for x in args]
    except ValueError:
        print("please run ah.py QUANTITY PRICE ONE_HOUR. all parameters integers. use 1 or 0 for one_hour")
        sys.exit()
    sell(args[0], args[1], args[2])
