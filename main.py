from cooldown import CoolDown, TooSoon
from pynput import keyboard
from phue import Bridge
import time


@CoolDown(0.5)
def toggle_lights():
    print('Toggling lights on/off')
    for l in lights:
        if l.on:
            l.on = False
        else:
            l.on = True


@CoolDown(0.25)
def lower_brightness():
    print('Lowering brightness')
    for l in lights:
        if l.brightness >= 10:
            l.brightness -= 10


@CoolDown(0.25)
def raise_brightness():
    print('Raising brightness')
    for l in lights:
        if l.brightness <= 245:
            l.brightness += 10


@CoolDown(0.5)
def activate_scene(group, scene):
    print('Setting scene ' + scene)
    if b.run_scene(group_name=group, scene_name=scene):
        print('Scene set')
    else:
        print('Setting scene failed')


def press_callback(key):
    if key == keyboard.Key.esc:
        # returning false in the callback stops the process
        return False

    if key == keyboard.Key.f21:
        try:
            toggle_lights()
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f23:
        try:
            lower_brightness()
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f22:
        try:
            raise_brightness()
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f15:
        try:
            activate_scene('[group name]', '[scene name]')
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f16:
        try:
            activate_scene('[group name]', '[scene name]')
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f17:
        try:
            activate_scene('[group name]', '[scene name]')
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f18:
        try:
            activate_scene('[group name]', '[scene name]')
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f19:
        try:
            print('Setting scene 5')
        except TooSoon as e:
            print(e)

    if key == keyboard.Key.f20:
        try:
            print('Setting scene 6')
        except TooSoon as e:
            print(e)


print('Please press the button on the bridge within 10 seconds')
time.sleep(10)

print('Trying connection')
try:
    b = Bridge('[your bridge ip here]')
    b.connect()
except:
    print('Connection failed')
else:
    print('Bridge connected')

lights = b.lights

l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()