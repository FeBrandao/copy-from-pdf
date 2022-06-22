import pyperclip
import keyboard
import time

def clean_clipboard_text():
    time.sleep(0.5)
    
    text = pyperclip.paste()

    pyperclip.copy(text.replace('\r\n', ' '))

keyboard.add_hotkey('ctrl+c', clean_clipboard_text)

while True:
    keyboard.wait()