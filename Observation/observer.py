class Observer:
    def __init__(self, observable):
        observable.register_observer(self)
        
    def notify(self, information=None):
        print("Received message!")
