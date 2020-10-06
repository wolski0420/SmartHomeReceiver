from GUI.HomeObjects.tobject import *


class TDoor(TObj):
    def __init__(self, obj, master=None):
        TObj.__init__(self, obj, master)
        self.__update_power_property_status__()
    
    def __update_power_property_status__(self):
        self._power_property_status_label.configure(text="blockade=" + str(self.obj.get_power()))
        self._power_property_status_label.configure(foreground="red")
        sleep(0.5)
        self._power_property_status_label.configure(foreground="black")
