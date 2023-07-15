from pynput import keyboard


# Define the mappings between keys and special characters
special_chars = {
    '1': '!',
    '2': '@',
    '3': '#',
    '4': '$',
    '5': '%',
    '6': '^',
    '7': '&',
    '8': '*',
    '9': '(',
    '0': ')',
    '-': '_',
    '=': '+',
    '[': '{',
    ']': '}',
    '\\': '|',
    ';': ':',
    "'": '"',
    ',': '<',
    '.': '>',
    '/': '?'
}

# keep track of the state of the capslock key the lazy way
# bool represents whether the key is down or not
global CAPSSTATE
CAPSSTATE = False

def on_key_press(key):
    global CAPSSTATE

    try:
        if key == keyboard.Key.caps_lock:
            CAPSSTATE = True
        elif CAPSSTATE and key.char in special_chars.keys():
            special_char = special_chars.get(key.char)
            keyboard.Controller().tap(keyboard.Key.backspace)
            keyboard.Controller().tap(special_char)
    except AttributeError:
        pass


def on_key_release(key):
    global CAPSSTATE

    if key == keyboard.Key.caps_lock:
        CAPSSTATE = False


with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()