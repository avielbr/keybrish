from keyboard import add_hotkey, wait
from pyperclip import copy, paste
from mappings import Mappings
from pyautogui import hotkey
from time import sleep

def flip():
    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    sleep(0.1)

    text = paste()

    if ord(text[0]) > 128 or text[0].isupper():
        copy(text.translate(Mappings.heb_eng))

    else: 
        copy(text.strip().translate(Mappings.eng_heb))

    hotkey('ctrl', 'v')

if __name__ == '__main__':
    add_hotkey('ctrl+\\', flip)
    wait()