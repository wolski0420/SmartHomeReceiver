class Behaviours:
    def __init__(self, subscriber, publisher, rooms, doors, alarms):
        self.subscriber = subscriber
        self.publisher = publisher
        self.rooms = rooms
        self.doors = doors
        self.alarms = alarms

    def __on_message__(self, client, user_data, msg):
        topic = msg.topic.split('/')
        message = str(msg.payload.decode('utf-8')).split('=')
        
        if topic[0] == 'door':
            door = self.doors[topic[1]]
            if door is None:
                return
            
            if message[0] == 'blockade_status':
                door.change_power(message[1])
                
        elif topic[0] == 'alarm':
            alarm = self.alarms[topic[1]]
            if alarm is None:
                return
            
            if message[0] == 'power':
                alarm.change_power(message[1])
                
        elif topic[0] == 'room':
            room = self.rooms[topic[1]]
            if room is None:
                return
            
            
            if topic[2] == 'light':
                light = room.lighting[topic[3]]
                if light is None:
                    return
                
                if message[0] == 'power':
                    light.change_power(message[1])
                elif message[0] == 'brightness':
                    light.change_brightness(message[1])
                elif message[0] == 'color':
                    light.change_brightness(message[1])
                    
            elif topic[2] == 'device':
                device = room.devices[topic[3]]
                if device is None:
                    return
                
                if message[0] == 'power':
                    device.change_power(message[1]) 
        
    def set_on_message(self):
        self.subscriber.on_message = self.__on_message__
        
    def on_close(self):
        for room in self.rooms.values():
            for light in room.lighting.values():
                self.publisher.publish(light.path, "power=off")
            for device in room.devices.values():
                self.publisher.publish(device.path, "power=off")
        for door in self.doors.values():
            self.publisher.publish(door.path, "blockade_status=unblock")
        for alarm in self.alarms.values():
            self.publisher.publish(alarm.path, "power=off")
            
    def set_all(self):
        self.set_on_message()
