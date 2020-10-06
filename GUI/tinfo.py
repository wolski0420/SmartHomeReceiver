from tkinter import Frame, Label, LEFT
from Observation.observer import Observer


class TInfo(Frame, Observer):
    def __init__(self, info, master=None):
        Frame.__init__(self, master=master)
        Observer.__init__(self, info)
        self.__info = info
        self.__info_label = Label(self, text="Connection information", font="Ubuntu 16 bold")
        self.__ip_port_frame = Frame(self)
        self.__ip_property_label = Label(self.__ip_port_frame, text='Address IP: ')
        self.__ip_value_label = Label(self.__ip_port_frame, text=self.__info.ip, background='orange')
        self.__port_property_label = Label(self.__ip_port_frame, text='   Port: ')
        self.__port_value_label = Label(self.__ip_port_frame, text=self.__info.port, background='orange')
        self.__setup_all__()
        
    def __setup_all__(self):
        self.__info_label.pack(pady=8)
        self.__ip_port_frame.pack(pady=6)
        self.__ip_property_label.pack(side=LEFT, padx=3)
        self.__ip_value_label.pack(side=LEFT, padx=3)
        self.__port_property_label.pack(side=LEFT, padx=3)
        self.__port_value_label.pack(side=LEFT, padx=3)
        
    def notify(self, information=None):
        self.__ip_value_label.configure(text=self.__info.ip)
        self.__port_value_label.configure(text=self.__info.port)
    