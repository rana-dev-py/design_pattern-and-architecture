"""A factory method chooses a concrete notifier."""
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message): pass

class Email(Notifier):
    def send(self, message): return f"email: {message}"

class NotifierFactory:
    def create(self, channel):
        return {"email": Email()}[channel]

print(NotifierFactory().create("email").send("Hello"))
