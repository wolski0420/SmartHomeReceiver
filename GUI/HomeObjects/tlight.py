from GUI.HomeObjects.tobject import *


class TLight(TObj):
    def __init__(self, obj, master=None):
        TObj.__init__(self, obj, master)
        self._brightness_property_status_label = None
        self.__set_brightness_property__()
        self._color_property_status_label = None
        self.__set_color_property__()
        
    def __set_brightness_property__(self):
        self._brightness_property_status_label = Label(self, text="brightness=" + str(self.obj.brightness))
        self._brightness_property_status_label.pack(side=LEFT, padx=3)
        
    def __set_color_property__(self):
        self._color_property_status_label = Label(self)
        self._color_property_status_label.pack(side=LEFT, padx=3)
        self.__update_color_property_status__()
        
    def __update_brightness_property_status__(self):
        self._brightness_property_status_label.configure(text="brightness=" + str(self.obj.brightness))
        self._brightness_property_status_label.configure(foreground="red")
        sleep(0.5)
        self._brightness_property_status_label.configure(foreground="black")
        
    def __update_color_property_status__(self):
        if self.obj.current_color is not None:
            self._color_property_status_label.configure(text="color=" + str(self.obj.current_color))
            self._color_property_status_label.configure(foreground="red")
            sleep(0.5)
            self._color_property_status_label.configure(foreground="black")
        else:
            self._color_property_status_label.configure(text="color=None")

    def notify(self, information=None):
        if information is None:
            return
        elif information == 'power':
            self.__update_power_property_status__()
        elif information == 'brightness':
            self.__update_brightness_property_status__()
        elif information == 'color':
            self.__update_color_property_status__()
    