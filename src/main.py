#!/usr/bin/env python3
import requests
import pyperclip
from pynput import keyboard


# *** Fetches the latest entry in the database
def fetch():
    # Currently fetches all the data from a database and copys the last value
    fetch = requests.get('http://192.168.128.241:5000/fetch')
    final = fetch.json()
    pyperclip.copy(final[-1][1])

# *** takes current clipboard and sends it to the server *** 
def post():
    clipboard_value = pyperclip.paste()
    post = requests.get(f'http://192.168.128.241:5000/post?content={clipboard_value}')

with keyboard.GlobalHotKeys({
        '<alt>+<ctrl>+p': post,
        '<alt>+<ctrl>+f': fetch}) as h:
    h.join()
