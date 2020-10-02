from Engine.HomeObjects.object import *


class Device(Obj):
    def __init__(self, name, path, pin):
        Obj.__init__(self, path, pin)
        self.name = name
