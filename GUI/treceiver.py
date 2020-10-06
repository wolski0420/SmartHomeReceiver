from tkinter import ttk
from GUI.tinfo import *
from GUI.tconnect import *
from GUI.HomeObjects.talarm import *
from GUI.HomeObjects.tdoor import *
from GUI.HomeObjects.tdevice import *
from GUI.HomeObjects.tlight import *
from tkinter import Label


class TReceiver:
    def __init__(self, receiver):
        self.receiver = receiver
        self.window = Tk()
        self.connect_window = TConnectWindow(self.receiver.info, self.__run__, self.__finish__)
        self.tinfo_frame = TInfo(self.receiver.info, self.window)
        self.tobjects_label = Label(self.window, text="Home Objects' Statuses", font="Ubuntu 16 bold")
        self.tobjects = []
        self.__setup__()

    def __setup__(self):
        self.__setup_window__()
        self.__setup_frames__()
        self.__setup_tobjects__()

    def __setup_window__(self):
        self.window.title(str('Receiver ' + self.receiver.name))
        self.window.protocol("WM_DELETE_WINDOW", self.__finish__)

    def __setup_frames__(self):
        self.tinfo_frame.pack(fill='both', padx=8)
        
    def __setup_tobjects__(self):
        self.tobjects_label.pack(pady=8)
        for alarm in self.receiver.alarms.values():
            t_alarm = TAlarm(alarm, self.window)
            t_alarm.pack(pady=6)
            self.tobjects.append(t_alarm)
        for door in self.receiver.doors.values():
            t_door = TDoor(door, self.window)
            t_door.pack(pady=6)
            self.tobjects.append(t_door)
        for room in self.receiver.rooms.values():
            for device in room.devices.values():
                t_device = TDevice(device, self.window)
                t_device.pack(pady=6)
                self.tobjects.append(t_device)
            for light in room.lighting.values():
                t_light = TLight(light, self.window)
                t_light.pack(pady=6)
                self.tobjects.append(t_light)

    def __run__(self):
        self.connect_window.destroy()
        self.receiver.run()
        self.window.update()
        self.window.deiconify()
        self.window.mainloop()

    def start(self):
        self.window.withdraw()
        self.connect_window.mainloop()

    def __finish__(self):
        self.window.destroy()
        self.receiver.finish()