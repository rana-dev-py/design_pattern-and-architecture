"""Creator subclasses provide their own product."""
from abc import ABC, abstractmethod

class Dialog(ABC):
    def render(self): return self.create_button().draw()
    @abstractmethod
    def create_button(self): pass

class WebDialog(Dialog):
    def create_button(self): return type("Button", (), {"draw": lambda s: "HTML button"})()

print(WebDialog().render())
