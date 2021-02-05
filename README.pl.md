# Smart Home Receiver

Wybierz język opisu: [PL](https://github.com/wolski0420/SmartHomeReceiver/blob/master/README.pl.md), [ENG](https://github.com/wolski0420/SmartHomeReceiver/blob/master/README.md)

Jest to aplikacja służąca jako odbiornik poleceń systemu inteligentnego domu. 
Umożliwia połączenie się poprzez sieć do naszego systemu i odbieranie poleceń, 
które mają np. uaktywnić alarm bądź wyłączyć światło w pokoju. 
Graficzny interfejs w tkinter, komunikacja między klientem a serwerem odbywa się za pomocą MQTT. 
Do uruchomienia nalezy mieć układ Raspberry Pi orazz zainstalowanego pythona i mosquitto (MQTT) na tym układzie. 
Po pobraniu całej aplikacji, w głównym katalogu należy wykonać w konsoli polecenie "python main.py". 
Pojawi się wtedy okienko logowania - należy wpisać odpowiedni adres ip i port serwera. 
Następnie pojawi się okienko odbiornika na którym widać statusy podłączonych urządzeń. Więcej informacji w dokumentacji:
[polska dokumentacja](https://github.com/wolski0420/SmartHomeReceiver/blob/master/Documentation-PL.pdf),
[english documentation](https://github.com/wolski0420/SmartHomeReceiver/blob/master/Documentation-ENG.pdf)
