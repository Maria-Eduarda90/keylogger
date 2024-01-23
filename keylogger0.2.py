import keyboard
from time import sleep

def capture_event(e):
    with open('mapping_keys.txt', 'a') as f:
        f.write(e.name)
        print(e.name)

keyboard.on_press(capture_event)
while True: sleep(1e6)