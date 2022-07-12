import pyperclip
import keyboard
import time

def clean_clipboard_text():
    time.sleep(0.8)
    
    text = pyperclip.paste()
    
    text = text.replace('\r\n', ' ')
    
    text = text.replace(' (A) ', '')
    text = text.replace(' (B) ', ';')
    text = text.replace(' (C) ', ';')
    text = text.replace(' (D) ', ';')
    text = text.replace(' (E) ', ';')
    
    text = text.replace(' (A)', '')
    text = text.replace(' (B)', ';')
    text = text.replace(' (C)', ';')
    text = text.replace(' (D)', ';')
    text = text.replace(' (E)', ';')
    
    text = text.replace('(A) ', '')
    text = text.replace('(B) ', ';')
    text = text.replace('(C) ', ';')
    text = text.replace('(D) ', ';')
    text = text.replace('(E) ', ';')
        
    text = text.replace('\r\n(A) ', '')
    text = text.replace('\r\n(B) ', ';')
    text = text.replace('\r\n(C) ', ';')
    text = text.replace('\r\n(D) ', ';')
    text = text.replace('\r\n(E) ', ';')
    
    text = text.replace('(A)', '')
    text = text.replace('(B)', ';')
    text = text.replace('(C)', ';')
    text = text.replace('(D)', ';')
    text = text.replace('(E)', ';')

    pyperclip.copy(text)

keyboard.add_hotkey('ctrl+c', clean_clipboard_text)

while True:
    keyboard.wait()
