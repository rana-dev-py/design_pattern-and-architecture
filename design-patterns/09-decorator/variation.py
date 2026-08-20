"""Decorators can be stacked."""
class Coffee:
    def cost(self): return 2
class Milk:
    def __init__(self, drink): self.drink = drink
    def cost(self): return self.drink.cost() + 1

print(Milk(Milk(Coffee())).cost())
