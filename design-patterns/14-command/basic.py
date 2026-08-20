"""Commands encapsulate operations."""
class Light:
    def on(self): return "light on"
class TurnOn:
    def __init__(self, light): self.light = light
    def execute(self): return self.light.on()

print(TurnOn(Light()).execute())
