from Engine.HomeObjects.object import *


class Door(Obj):
    def __init__(self, room1, room2, pin):
        Obj.__init__(self, str(f'door/{room1.name}-{room2.name}'), pin)
        self.room1 = room1
        self.room2 = room2
        
    def __setup__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.change_power('unblock')
    
    def change_power(self, signal):
        signal = signal.lower()
        if signal == 'block':
            GPIO.output(self.pin, GPIO.HIGH)
        else:
            GPIO.output(self.pin, GPIO.LOW)
            
        opposite = signal
        if opposite == 'block':
            opposite = 'unblock'
        else:
            opposite = 'block'
                
        signal, opposite = signal.capitalize(), opposite.capitalize()
            
        print(f'Changed power status in \"{self.path}\" '
              f'from \"{opposite}\" to \"{signal}\"')
