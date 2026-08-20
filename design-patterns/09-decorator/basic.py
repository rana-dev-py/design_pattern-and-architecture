"""Wrap a service to add logging."""
class Service:
    def fetch(self): return "data"
class LoggingService:
    def __init__(self, wrapped): self.wrapped = wrapped
    def fetch(self):
        print("fetching")
        return self.wrapped.fetch()

print(LoggingService(Service()).fetch())
