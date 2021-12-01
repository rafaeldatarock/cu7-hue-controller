from pynput import keyboard
from phue import Bridge
import time

from cooldown import CoolDown, TooSoon

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
        print('Setting scene 1')
    
    if key == keyboard.Key.f16:
        print('Setting scene 2')

    if key == keyboard.Key.f17:
        print('Setting scene 3')

    if key == keyboard.Key.f18:
        print('Setting scene 4')

    if key == keyboard.Key.f19:
        print('Setting scene 5')

    if key == keyboard.Key.f20:
        print('Setting scene 6')


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
# api = b.get_api()


l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()