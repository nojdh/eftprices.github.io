import cv2
import pytesseract
import pyautogui
import time
import winsound
import os
import json

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

item_list_dict = {
  "6b47 ratnik-bsh helmet": 0,
  "Pack of sugar": 0,
   "Lab. Red keycard": 0,
  "Military cable": 0,
  "Paracord": 0,
  "Corrugated hose": 0,
  "Gas analyzer": 0,
  "SSD drive": 0,
  "Military COFDM wireless Signal Transmitter": 0,
  "Wires": 0,
  "Car battery": 0,
  }


def ocr_core(filename):
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imagem = cv2.bitwise_not(image)
    text = pytesseract.image_to_string(imagem, lang = 'Bender', config='outputbase digits')
    return text

def mouseMovement(itemname):
    pyautogui.moveTo(100, 120)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(itemname, interval=0.07)
    pyautogui.hotkey('space')
    time.sleep(1)
    pyautogui.hotkey('backspace')
    time.sleep(1)
    pyautogui.moveTo(120, 160)
    pyautogui.click()
    pyautogui.hotkey('F5')
    time.sleep(2)

def screenshotCaptures(itemname):
    myScreenshot = pyautogui.screenshot(region=(1240,300, 200, 40))
    myScreenshot.save(f'{itemname}.png')
    myScreenshot2 = pyautogui.screenshot(region=(1240,375, 200, 40))
    myScreenshot2.save(f'{itemname}2.png')
    myScreenshot2 = pyautogui.screenshot(region=(1240,450, 200, 40))
    myScreenshot2.save(f'{itemname}3.png')

def ocrTextat(itemname):
    value1 = ocr_core(f'{itemname}.png').replace(" ", "")[:-1]
    value2 = ocr_core(f'{itemname}2.png').replace(" ", "")[:-1]
    value3 = ocr_core(f'{itemname}3.png').replace(" ", "")[:-1]
    try:
        data = int(value1) + int(value2) + int(value3)
    except ValueError:
        data = float(value1) + float(value2) + float(value3)
    average = data / 3
    averageround = round(average)
    averagefinal = f'{averageround:,}'
    return averagefinal

def checkPrice(itemname):
    mouseMovement(itemname)
    screenshotCaptures(itemname)
    item_list_dict[itemname] = ocrTextat(itemname)
    winsound.Beep(500, 300)

def main():
    for k in item_list_dict:
        checkPrice(k)
    print(item_list_dict)
    with open('items.json', 'w') as fp:
        json.dump(item_list_dict, fp, indent=4, sort_keys=True)
    winsound.Beep(500, 300)
    winsound.Beep(500, 300)
    winsound.Beep(500, 300)

if __name__ == "__main__":
    main()


