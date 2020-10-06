import RPi.GPIO as GPIO
from Observation.observable import *
from datetime import datetime


class Light(Observable):
    def __init__(self, name, path, pin, power=False, brightness=50, colors=None):
        Observable.__init__(self)
        self.name = name
        self.pin = pin
        self.path = path
        self.power = power
        self.brightness = brightness    # 0-100 value
        self.pwm = None
        self.colors = []                # list of possibly colors in current light
        self.current_color = None
        self.__setup__()

        if colors:
            self.colors = colors
            self.current_color = colors[0]
            
    def __setup__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 100)
        self.pwm.start(0)
        self.change_power('off')
    
    def change_power(self, signal):
        signal = signal.lower()
        if signal == 'on':
            self.pwm.ChangeDutyCycle(self.brightness)
            self.power = True
        else:
            self.pwm.ChangeDutyCycle(0)
            self.power = False
            
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
        return "on" if self.power else "off"

    def change_brightness(self, signal):
        signal = int(signal)
        if 0 <= signal <= 100:
            self.brightness = signal
            if self.power:
                self.pwm.ChangeDutyCycle(self.brightness)
                
            file = open("logs.txt", "a")
            actual_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            file.write(f'[{actual_time}]  Changed brightness of \"{self.path}\" '
                  f'to \"{self.brightness}\"!!!\n')
            file.close()
                
            print(f'Changed brightness of \"{self.path}\" '
                  f'to \"{self.brightness}\"!!!')
            self.notify_observers('brightness')

    def change_color(self, signal):
        self.current_color = signal
        
        file = open("logs.txt", "a")
        actual_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write(f'[{actual_time}]  Changed color of \"{self.path}\" '
              f'to \"{self.current_color}\"!!!\n')
        file.close()
        
        print(f'Changed color of \"{self.path}\" '
              f'to \"{self.current_color}\"!!!')
        self.notify_observers('color')
