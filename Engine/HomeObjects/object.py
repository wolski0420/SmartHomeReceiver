import RPi.GPIO as GPIO


class Obj:
    def __init__(self, path, pin):
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
            
        print(f'Changed power status in \"{self.path}\" '
              f'from \"{opposite}\" to \"{signal}\"')
