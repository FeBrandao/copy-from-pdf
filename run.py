import pyperclip
import keyboard
import time

def clean_clipboard_text():
    time.sleep(0.8)
    
    text = pyperclip.paste()
    
    text.replace('\r\n', ' ')

    pyperclip.copy(text)

keyboard.add_hotkey('ctrl+c', clean_clipboard_text)

while True:
    keyboard.wait()
