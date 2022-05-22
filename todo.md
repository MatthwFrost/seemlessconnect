# Todo List
  - Create a program that can send text to different devices
  - Essentaily a NAS, Maybe yes a NAS that has a user interface
  - Create an api that can communicate between the server
  - Host the server on raspberry pi
  - A clipboard like program, like the posty windows app
  - How do I even approach this?
  - Possilby add the new stuff to the clipboard instead of a ui? Maybe both for multiple copy's
  - If Post() is run before fetch(), it will send what ever will be in the clipboard and will
    be in an endless loop.
  - How is the user going to interface with the program?
  -   A custom hotkey to copy to the programs clipboard?
        Will have to make own custom clipboard

### Clipboard
  - Command to copy the text to a cache
  - Take the coppied text and add that to the server
  - Hotkey to send the text
      CMD+C then CMD+Z to send the text

### Server
  - Request individual data

## Need to learn
  - Api's, sending and reciving data
  - hosting a server with data

### Run public
host="0.0.0.0"
or
Use local IP instead

#### Run as a background process
for masOS/Linux
nohup python main.py

for Windows

KILL:
pkill -f test.py
