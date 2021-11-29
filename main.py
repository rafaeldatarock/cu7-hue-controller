from pynput import keyboard

def press_callback(key):
    print('{} was pressed'.format(key))

def release_callback(key):
    print('{} released'.format(key))

l = keyboard.Listener(on_press=press_callback,on_release=release_callback)
l.start()
l.join()