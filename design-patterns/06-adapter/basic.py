"""Adapter makes a legacy API match the expected interface."""
class LegacyTemperature:
    def read_fahrenheit(self): return 77

class CelsiusAdapter:
    def __init__(self, legacy): self.legacy = legacy
    def read_celsius(self): return (self.legacy.read_fahrenheit() - 32) * 5 / 9

print(CelsiusAdapter(LegacyTemperature()).read_celsius())
