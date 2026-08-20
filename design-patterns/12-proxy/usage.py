"""Caching proxy avoids repeat calls."""
class WeatherAPI:
    def fetch(self, city): return f"sunny in {city}"
class CachedWeather:
    def __init__(self): self.api, self.cache = WeatherAPI(), {}
    def fetch(self, city): return self.cache.setdefault(city, self.api.fetch(city))

print(CachedWeather().fetch("Lahore"))
