import pyperclip
import keyboard
import time

def clean_clipboard_text():
    time.sleep(0.8)
    
    text = pyperclip.paste()
    
    text.replace('\r\n', ' ')
    
    text.replace('(A) ', ';')
    text.replace('(B) ', ';')
    text.replace('(C) ', ';')
    text.replace('(D) ', ';')
    text.replace('(E) ', ';')
    
    text.replace('\r\n(A) ', ';')
    text.replace('\r\n(B) ', ';')
    text.replace('\r\n(C) ', ';')
    text.replace('\r\n(D) ', ';')
    text.replace('\r\n(E) ', ';')

    pyperclip.copy(text)

keyboard.add_hotkey('ctrl+c', clean_clipboard_text)

while True:
    keyboard.wait()
