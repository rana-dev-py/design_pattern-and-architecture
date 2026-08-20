"""Visitor separates an operation from element classes."""
class Number:
    def __init__(self, value): self.value = value
    def accept(self, visitor): return visitor.visit_number(self)
class Printer:
    def visit_number(self, number): return str(number.value)

print(Number(7).accept(Printer()))
