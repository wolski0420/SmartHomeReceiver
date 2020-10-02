class Room:
    def __init__(self, name, lighting=None, devices=None):
        if lighting is None:
            lighting = []
        if devices is None:
            devices = []
        self.name = name
        self.lighting = lighting
        self.devices = devices
