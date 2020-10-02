from Engine.HomeObjects.object import *


class Alarm(Obj):
    def __init__(self, name, path, pin):
        Obj.__init__(self, str(f'alarm/{path}'), pin)
        self.name = name
