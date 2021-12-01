from pynput import keyboard
from phue import Bridge

b = Bridge('')
lights = b.lights
api = b.get_api()

def press_callback(key):
    if key == keyboard.Key.esc:
        # returning false in the callback stops the process
        return False

    if key == keyboard.Key.f21:
        print('Toggling lights on/off')
        if b.get_light(['Hanglamp','Strip','Spotje'], 'on'):
            b.set_light(['Hanglamp','Strip','Spotje'], 'on', False)
        
        if not b.get_light(['Hanglamp','Strip','Spotje'], 'on'):
            b.set_light(['Hanglamp','Strip','Spotje'], 'on', True)

    if key == keyboard.Key.f23:
        print('Lowering brightness')
        for l in lights:
            l.brightness -= 1

    if key == keyboard.Key.f22:
        print('Raising brightness')
        for l in lights:
            l.brightness += 1

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

l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()