import keyboard

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

def on_key_press(event):
    if event.event_type == 'down':
        if keyboard.is_pressed('caps lock'):
            if event.name in special_chars.keys():  # check for Alt + special character key
                special_char = special_chars.get(event.name)  # get the corresponding special character
                keyboard.write('\b')  # type the special character
                keyboard.write(special_char)  # type the special character
                keyboard.press_and_release('caps lock')

keyboard.on_press(on_key_press)

# Run the event listener loop
keyboard.wait()