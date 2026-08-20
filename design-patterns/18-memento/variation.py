"""Caretaker keeps a history of snapshots."""
class Counter:
    def __init__(self): self.value = 0
    def snapshot(self): return self.value
    def restore(self, state): self.value = state

counter = Counter(); history = [counter.snapshot()]; counter.value = 5; counter.restore(history.pop()); print(counter.value)
