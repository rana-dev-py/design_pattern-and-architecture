"""Singleton through a module: Python's simplest shared object."""
class Registry:
    services = {}

registry = Registry()
registry.services["mailer"] = "smtp"
print(registry.services)
