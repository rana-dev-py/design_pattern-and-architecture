"""Commands can support undo."""
class Counter:
    def __init__(self): self.value = 0
class Add:
    def __init__(self, counter, amount): self.counter, self.amount = counter, amount
    def execute(self): self.counter.value += self.amount
    def undo(self): self.counter.value -= self.amount

c = Counter(); command = Add(c, 5); command.execute(); command.undo(); print(c.value)
