import paho.mqtt.client as mqtt
import Engine.ConfigSetup.parser as parser
from Engine.behaviours import Behaviours
from Engine.info import Info
from time import sleep
import RPi.GPIO as GPIO


class Receiver:
    def __init__(self, name):
        self.name = name
        self.rooms = parser.setup_rooms()
        self.doors = parser.setup_doors(self.rooms)
        self.alarms = parser.setup_alarms()
        self.subscriber = mqtt.Client()
        self.publisher = mqtt.Client()
        self.behaviours = None
        self.info = Info("127.0.0.1", 1883)
        
    def __subscribe_all__(self):
        for room in self.rooms.values():
            for light in room.lighting.values():
                self.subscriber.subscribe(light.path)
            for device in room.devices.values():
                self.subscriber.subscribe(device.path)
        for door in self.doors.values():
            self.subscriber.subscribe(door.path)
        for alarm in self.alarms.values():
            self.subscriber.subscribe(alarm.path)
            
    def __setup_client__(self):
        self.behaviours = Behaviours(self.subscriber, self.publisher, self.rooms, self.doors, self.alarms)
        self.behaviours.set_all()
        
    def __setup__(self):
        self.__setup_client__()
        self.__subscribe_all__()
        
    def run(self):
        self.subscriber.connect(self.info.ip, self.info.port)
        self.subscriber.loop_start()
        self.__setup__()
        
    def finish(self):
        self.subscriber.loop_stop()
        
        if self.behaviours is not None:
            self.publisher.connect(self.info.ip, self.info.port)
            self.behaviours.on_close()
            self.publisher.disconnect()
            
        self.subscriber.disconnect()
        GPIO.cleanup()
