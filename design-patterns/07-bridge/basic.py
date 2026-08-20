"""Abstraction delegates to an independently varying implementation."""
class ConsoleDevice:
    def power(self): return "console powered"
class Radio:
    def __init__(self, device): self.device = device
    def turn_on(self): return self.device.power()

print(Radio(ConsoleDevice()).turn_on())
