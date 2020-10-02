import paho.mqtt.client as mqtt
import ConfigSetup.parser as parser
from behaviours import *
from time import sleep


class Receiver:
    def __init__(self, name, ip="127.0.0.1", port=1883):
        self.name = name
        self.rooms = parser.setup_rooms()
        self.doors = parser.setup_doors(self.rooms)
        self.alarms = parser.setup_alarms()
        self.subscriber = mqtt.Client()
        self.ip = ip
        self.port = port
        
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
        Behaviours(self.subscriber, self.rooms, self.doors, self.alarms).set_all()
        
    def __setup__(self):
        self.__setup_client__()
        self.__subscribe_all__()
        
    def run(self):
        self.subscriber.connect(self.ip, self.port)
        self.subscriber.loop_start()
        self.__setup__()
        
    def finish(self):
        self.subscriber.loop_stop()
        self.subscriber.disconnect()

rc = Receiver('Odbiornik')
rc.run()
sleep(120)
rc.finish()
