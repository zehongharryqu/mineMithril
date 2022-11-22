import pyautogui
import time
import sys
import bzcoords as bzc

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print("please run bz.py ITEM #_OF_ORDERS PRICE")
        sys.exit()
    item = args[0]
    orders = int(args[1])
    while orders:
        time.sleep(2)
        pyautogui.write('/bz', interval=0.25)
        pyautogui.press('enter')
        time.sleep(1)
        coords_list = bzc.COORDS.find(item)
        coords_list = coords_list[1:]
        if coords_list:
            for c in coords_list:
                pyautogui.click(*c)
                time.sleep(0.5)
        else:
            print("that item is not supported :c")
            sys.exit()
        time.sleep(0.5)
        pyautogui.click(*bzc.BUY)
        time.sleep(0.5)
        pyautogui.moveTo(*bzc.AMOUNT)
        pyautogui.click()
        time.sleep(1)
        pyautogui.write('71680', interval=0.25)
        time.sleep(0.5)
        pyautogui.click(*bzc.DONE)
        time.sleep(0.5)
        pyautogui.moveTo(*bzc.AMOUNT)
        pyautogui.click()
        time.sleep(1)
        pyautogui.write(args[2], interval=0.25)
        time.sleep(0.5)
        pyautogui.click(*bzc.DONE)
        time.sleep(0.5)
        pyautogui.click(*bzc.CONFIRM)
        orders -= 1
