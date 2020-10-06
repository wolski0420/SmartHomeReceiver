import RPi.GPIO as GPIO
from Observation.observable import *
from datetime import datetime


class Obj(Observable):
    def __init__(self, path, pin):
        Observable.__init__(self)
        self.pin = pin
        self.path = path
        self.__setup__()
        
    def __setup__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.change_power('off')
    
    def change_power(self, signal):
        signal = signal.lower()
        if signal == 'on':
            GPIO.output(self.pin, GPIO.HIGH)
        else:
            GPIO.output(self.pin, GPIO.LOW)
            
        opposite = signal
        if opposite == 'on':
            opposite = 'off'
        else:
            opposite = 'on'
                
        signal, opposite = signal.capitalize(), opposite.capitalize()
        
        file = open("logs.txt", "a")
        actual_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write(f'[{actual_time}]  Changed power status in \"{self.path}\" '
              f'from \"{opposite}\" to \"{signal}\"\n')
        file.close()
        
        print(f'Changed power status in \"{self.path}\" '
              f'from \"{opposite}\" to \"{signal}\"')
        self.notify_observers('power')
        
    def get_power(self):
        return "on" if GPIO.input(self.pin) else "off"
