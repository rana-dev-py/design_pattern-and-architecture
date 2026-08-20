"""Facade hides subsystem coordination."""
class Inventory:
    def available(self, item): return True
class Payment:
    def charge(self): return True
class Checkout:
    def buy(self, item):
        return "ordered" if Inventory().available(item) and Payment().charge() else "failed"

print(Checkout().buy("book"))
