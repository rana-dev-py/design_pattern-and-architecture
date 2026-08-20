"""Composite expressions implement grammar rules."""
class Number:
    def __init__(self, value): self.value = value
    def interpret(self): return self.value
class Add:
    def __init__(self, left, right): self.left, self.right = left, right
    def interpret(self): return self.left.interpret() + self.right.interpret()

print(Add(Number(2), Number(3)).interpret())
