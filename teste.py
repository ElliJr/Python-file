import keyboard

def on_press(keu):
    print('Key pressed: {0}'.format(keu))

keyboard.on_press(on_press)
keyboard.wait()