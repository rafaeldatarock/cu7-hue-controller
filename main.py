import configparser
import time

from cooldown import TooSoon
from actions import *

from pynput import keyboard
from phue import Bridge, Scene

# Reading from config file
cfg = configparser.ConfigParser()
cfg.read('config.ini')
try:
    bridge_ip = cfg['bridge']['IP']

    first_run = cfg.getboolean('init', 'Running_on_new_device')

    scene_1 = cfg['scene_1']
    scene_2 = cfg['scene_2']
    scene_3 = cfg['scene_3']
    scene_4 = cfg['scene_4']
    scene_5 = cfg['scene_5']
    scene_6 = cfg['scene_6']
except KeyError as e:
    print(e)


# Defining what to do when a key is pressed
def press_callback(key):
    if key == keyboard.Key.esc:
        # returning false in the callback stops the process
        return False

    try:
        # Checking if pressed key is present in
        trigger = triggers.get(key, False)
        if trigger:
            function = trigger['f']
            params = trigger['p']
            function(*params)
    except TooSoon as e:
        print(e)


# Give some time to press the button on the bridge
if first_run:
    print('Please press the button on the bridge within 10 seconds')
    time.sleep(15)

# Making connection with bridge
print('Trying to connect to bridge')
try:
    b = Bridge(bridge_ip)
    if first_run:
        # If first run on device, call Bridge.connect() to register application and device on the bridge
        b.connect()
except:
    print('Connection failed')
else:
    print('Bridge connected')


# Selects all lights connected to the bridge, so they can be looped over
# I will replace this with selecting specific lights which will be able set in config.ini
lights = b.lights

# Defining the trigger functions and their parameters
triggers = {
    keyboard.Key.f21: { 'f': toggle_lights, 'p': [lights] },
    keyboard.Key.f23: { 'f': lower_brightness, 'p': [lights] },
    keyboard.Key.f22: { 'f': raise_brightness, 'p': [lights] },
    keyboard.Key.f15: { 'f': activate_scene, 'p': [b, scene_1.get('Group', ''), scene_1.get('Scene', '')] },
    keyboard.Key.f16: { 'f': activate_scene, 'p': [b, scene_2.get('Group', ''), scene_2.get('Scene', '')] },
    keyboard.Key.f17: { 'f': activate_scene, 'p': [b, scene_3.get('Group', ''), scene_3.get('Scene', '')] },
    keyboard.Key.f18: { 'f': activate_scene, 'p': [b, scene_4.get('Group', ''), scene_4.get('Scene', '')] },
    keyboard.Key.f19: { 'f': activate_scene, 'p': [b, scene_5.get('Group', ''), scene_5.get('Scene', '')] },
    keyboard.Key.f20: { 'f': activate_scene, 'p': [b, scene_6.get('Group', ''), scene_6.get('Scene', '')] },
}

# Creating and starting the keyboard listener
l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()
