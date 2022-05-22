#!/usr/bin/env python3
import requests
import pyperclip
from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='Z')}
]
# The currently active modifiers
current = set()

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            post()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

def fetch():
    # Currently fetches all the data from a database and copys the last value
    fetch = requests.get('http://192.168.128.241:5000/fetch')
    print(fetch)
    print(fetch.json())
    final = fetch.json()[-1][1]
    pyperclip.copy(final)
    return final

# *** takes current clipboard and sends it to the server *** 
def post():
    clipboard_value = pyperclip.paste()
    post = requests.get(f'http://192.168.128.241:5000/post?content={clipboard_value}')
    return clipboard_value

def main():

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    print(fetch())

if __name__ == '__main__':
    main()

