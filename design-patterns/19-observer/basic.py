"""Subject notifies subscribed observers."""
class Subject:
    def __init__(self): self.observers = []
    def subscribe(self, observer): self.observers.append(observer)
    def notify(self, value):
        for observer in self.observers: observer(value)

subject = Subject(); subject.subscribe(lambda value: print("got", value)); subject.notify(42)
