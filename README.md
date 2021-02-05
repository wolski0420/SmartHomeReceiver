# Smart Home Remote Control

Choose description language: [PL](https://github.com/wolski0420/SmartHomeReceiver/blob/master/README.pl.md), [ENG](https://github.com/wolski0420/SmartHomeReceiver/blob/master/README.md)

This is the application used as command receiver and executor to smart home. It allows you to connect to your home system and receive commands from remote controls, 
then you will be able to see the effect on connected devices. GUI in tkinter, communication between client and server is run by MQTT.
To start this app, you need to have Raspberry Pi and python with mosquitto (MQTT) installed on RPi. After downloading all the packages, enter "python main.py"
in console from main directory. It will show connection window where you need to enter server ip address and port. 
Then you will be able to see a window where you can see all connected devices statuses. More information in the documentation:
[polska dokumentacja](https://github.com/wolski0420/SmartHomeReceiver/blob/master/Documentation-PL.pdf),
[english documentation](https://github.com/wolski0420/SmartHomeReceiver/blob/master/Documentation-ENG.pdf)
