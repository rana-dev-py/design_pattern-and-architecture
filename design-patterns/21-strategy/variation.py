"""Strategies make pricing rules interchangeable."""
class Cart:
    def __init__(self, discount): self.discount = discount
    def total(self, amount): return amount * (1 - self.discount)

print(Cart(0.10).total(100))
