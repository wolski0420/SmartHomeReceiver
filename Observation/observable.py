class Observable:
    def __init__(self):
        self.__observers = []
        
    def register_observer(self, observer):
        self.__observers.append(observer)
        
    def notify_observers(self, information=None):
        for o in self.__observers:
            o.notify(information=information)
