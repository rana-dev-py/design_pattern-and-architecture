"""Iterator object stores traversal state."""
class StepIterator:
    def __init__(self, items): self.items, self.index = items, 0
    def __iter__(self): return self
    def __next__(self):
        if self.index == len(self.items): raise StopIteration
        item = self.items[self.index]; self.index += 1; return item

print(list(StepIterator(["a", "b"])))
