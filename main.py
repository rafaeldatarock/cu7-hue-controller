import configparser
import time

from cooldown import TooSoon
from actions import *

from pynput import keyboard
from phue import Bridge, Scene

# Reading from config file
cfg = configparser.ConfigParser()
try:
    cfg.read('config.ini')

    bridge_ip = cfg['bridge']['IP']

    first_run = cfg.getboolean('init', 'Running_on_new_device')

    scene_1 = cfg['scene_1']
    scene_2 = cfg['scene_2']
    scene_3 = cfg['scene_3']
    scene_4 = cfg['scene_4']
    scene_5 = cfg['scene_5']
    scene_6 = cfg['scene_6']
except Exception as e:
    print(e)


def press_callback(key):
    if key == keyboard.Key.esc:
        # returning false in the callback stops the process
        return False

    if key == keyboard.Key.f21:
        try:
            toggle_lights(lights)
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f23:
        try:
            lower_brightness(lights)
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f22:
        try:
            raise_brightness(lights)
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f15:
        try:
            activate_scene(b, scene_1['Group'], scene_1['Scene'])
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f16:
        try:
            activate_scene(b, scene_2['Group'], scene_2['Scene'])
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f17:
        try:
            activate_scene(b, scene_3['Group'], scene_3['Scene'])
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f18:
        try:
            activate_scene(b, scene_4['Group'], scene_4['Scene'])
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f19:
        try:
            activate_scene(b, scene_5['Group'], scene_5['Scene'])
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f20:
        try:
            activate_scene(b, scene_6['Group'], scene_6['Scene'])
        except TooSoon as e:
            print(e)


if first_run:
    print('Please press the button on the bridge within 10 seconds')
    time.sleep(10)

print('Trying connection')
try:
    b = Bridge(bridge_ip)
    if first_run:
        b.connect()
except:
    print('Connection failed')
else:
    print('Bridge connected')

lights = b.lights

l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()