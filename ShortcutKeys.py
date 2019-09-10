import os
from pynput.keyboard import Key, KeyCode, Listener

def lock_screen():
    os.popen('xdg-screensaver lock')

def test_function():
    print("Test function started.")

def open_chrome():
    os.popen("google-chrome")

combination_of_custom = {
    frozenset([Key.cmd, KeyCode(char='t')]): test_function,
    frozenset([Key.cmd, KeyCode(char='o')]): lock_screen,
    frozenset([Key.cmd, KeyCode(char='c')]): open_chrome
}

current=set()

def on_press(key):
    try:
        current.add(key)
        if frozenset(current) in combination_of_custom:
            combination_of_custom[frozenset(current)]()
    except Exception as ex:
        print("Exception(press) : ", ex)

def on_release(key):
    try:
        current.remove(key)
    except Exception as ex:
        print("Exception(release) : ", ex)

with Listener(on_press = on_press, on_release = on_release) as listener:
    try:
        listener.join()
    except Exception as ex:
        print("Exception.", ex)