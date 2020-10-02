from Engine.HomeObjects.object import *


class Light(Obj):
    def __init__(self, name, path, pin, power=False, brightness=50, colors=None):
        Obj.__init__(self, path, pin)
        self.brightness = brightness    # 0-100 value
        self.colors = []                # list of possibly colors in current light
        self.current_color = None

        if colors:
            self.colors = colors
            self.current_color = colors[0]

    def change_brightness(self, signal):
        signal = int(signal)
        if 0 <= signal <= 100:
            self.brightness = signal
            print(f'Changed brightness of \"{self.path}\" '
                  f'to \"{self.brightness}\"!!!')

    def change_color(self, signal):
        self.current_color = signal
        print(f'Changed color of \"{self.path}\" '
              f'to \"{self.current_color}\"!!!')
