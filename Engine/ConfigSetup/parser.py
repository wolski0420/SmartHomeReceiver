import sys
sys.path.append("..")


import json
from HomeObjects.device import *
from HomeObjects.room import *
from HomeObjects.light import *
from HomeObjects.door import *
from HomeObjects.alarm import *


ROOMS_CONFIG_PATH = "ConfigSetup/rooms.json5"
DOORS_CONFIG_PATH = "ConfigSetup/doors.json5"
ALARMS_CONFIG_PATH = "ConfigSetup/alarms.json5"


def setup_alarms():
    rc_config = json.load(open(ALARMS_CONFIG_PATH))
    alarms = dict()

    for alarm in rc_config:
        alarms[str(alarm["location"] + "-" + alarm["name"])] = Alarm(
            alarm["name"], str(alarm["location"] + "-" + alarm["name"]), alarm["pin"]
        )

    return alarms


def setup_doors(rooms):
    rc_config = json.load(open(DOORS_CONFIG_PATH))
    doors = dict()

    for door in rc_config:
        doors[str(door["room1"] + "-" + door["room2"])] = Door(
            rooms[door["room1"]], rooms[door["room2"]], door["pin"]
        )

    return doors


def setup_lighting(room):
    lights = dict()

    for light in room["lighting"]:
        lights[light["name"]] = Light(light["name"], str("room/" + room["name"] + "/light/" + light["name"]),
                                      light["pin"], colors=light["colors"])

    return lights


def setup_devices(room):
    devices = dict()

    for device in room["devices"]:
        devices[device["name"]] = Device(device["name"], str("room/" + room["name"] + "/device/" + device["name"]), device["pin"])

    return devices


def setup_rooms():
    rc_config = json.load(open(ROOMS_CONFIG_PATH))
    rooms = dict()

    for room in rc_config:
        rooms[room["name"]] = Room(room["name"], setup_lighting(room), setup_devices(room))

    return rooms
