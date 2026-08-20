"""A remote abstraction can work with another device implementation."""
class TV:
    def power(self): return "TV powered"
class Remote:
    def __init__(self, device): self.device = device
    def toggle(self): return self.device.power()

print(Remote(TV()).toggle())
