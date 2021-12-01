from cooldown import CoolDown

@CoolDown(0.5)
def toggle_lights(lights):
    print('Toggling lights on/off')
    for l in lights:
        if l.on:
            l.on = False
        else:
            l.on = True


@CoolDown(0.25)
def lower_brightness(lights):
    print('Lowering brightness')
    for l in lights:
        if l.brightness >= 10:
            l.brightness -= 10


@CoolDown(0.25)
def raise_brightness(lights):
    print('Raising brightness')
    for l in lights:
        if l.brightness <= 245:
            l.brightness += 10


@CoolDown(0.5)
def activate_scene(b, group, scene):
    print('Setting scene ' + scene)
    if b.run_scene(group_name=group, scene_name=scene):
        print('Scene set')
    else:
        print('Setting scene failed')