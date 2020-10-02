from Engine.receiver import *

rc = Receiver('Odbiornik')
rc.run()
sleep(120)
rc.finish()
