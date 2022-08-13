import pyautogui
import time
import sys
import bzcoords as bzc

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print("please run bz.py ITEM #_OF_ORDERS PRICE")
        sys.exit()
    orders = int(args[1])
    while orders:
        time.sleep(2)
        pyautogui.write('/bz', interval=0.25)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(*bzc.COORDS["mining"])
        time.sleep(0.2)
        if args[0] == "jade":
            pyautogui.click(*bzc.COORDS["gems"])
            time.sleep(0.2)
            pyautogui.click(*bzc.COORDS["jade"])
        elif args[0] == "topaz":
            pyautogui.click(*bzc.COORDS["gems"])
            time.sleep(0.2)
            pyautogui.click(*bzc.COORDS["topaz"])
        elif args[0] == "ice":
            pyautogui.click(*bzc.COORDS["ices"])
            time.sleep(0.2)
            pyautogui.click(*bzc.COORDS["ice"])
        else:
            print("that item not supported :c")
            sys.exit()
        time.sleep(0.2)
        pyautogui.click(*bzc.COORDS["buy"])
        time.sleep(0.2)
        pyautogui.moveTo(*bzc.COORDS["amount"])
        pyautogui.click()
        time.sleep(1)
        pyautogui.write('71680', interval=0.25)
        time.sleep(0.2)
        pyautogui.click(*bzc.COORDS["done"])
        time.sleep(0.2)
        pyautogui.moveTo(*bzc.COORDS["amount"])
        pyautogui.click()
        time.sleep(1)
        pyautogui.write(args[2], interval=0.25)
        time.sleep(0.2)
        pyautogui.click(*bzc.COORDS["done"])
        time.sleep(0.2)
        pyautogui.click(*bzc.COORDS["confirm"])
        orders -= 1
