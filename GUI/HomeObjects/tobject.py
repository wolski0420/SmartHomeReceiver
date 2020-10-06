from Observation.observer import *
from tkinter import Frame, Label, LEFT
from time import sleep


class TObj(Frame, Observer):
    def __init__(self, obj, master=None):
        Frame.__init__(self, master=master)
        Observer.__init__(self, obj)
        self.obj = obj
        self.pack()
        self._property_label = None
        self._power_property_status_label = None
        self.__set_power_property__()
        
    def __set_power_property__(self):
        self._property_label = Label(self, text=self.obj.path + "  ::::  ")
        self._property_label.pack(side=LEFT, padx=3)
        self._power_property_status_label = Label(self, text="power=" + str(self.obj.get_power()))
        self._power_property_status_label.pack(side=LEFT, padx=3)
        
    def __update_power_property_status__(self):
        self._power_property_status_label.configure(text="power=" + str(self.obj.get_power()))
        self._power_property_status_label.configure(foreground="red")
        sleep(0.5)
        self._power_property_status_label.configure(foreground="black")
        
    def notify(self, information=None):
        if information is None:
            return
        elif information == 'power':
            self.__update_power_property_status__()
