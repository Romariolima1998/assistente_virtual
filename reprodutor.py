import os
import pyautogui
import time

def reproduzir():
    os.system('start vlc.exe')
    time.sleep(2)
    pyautogui.hotkey('ctrl','f')
    time.sleep(2)
    pyautogui.press('enter')
    return

def play_pause():
    pyautogui.press('space')
    return

def proxima():
    pyautogui.press('n')
    return

def anterior():
    pyautogui.press('P')
    return

def fechar():
    pyautogui.hotkey('ctrl','q')
    return

