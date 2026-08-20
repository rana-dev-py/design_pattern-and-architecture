"""Choose a sorting algorithm at runtime."""
def ascending(items): return sorted(items)
def descending(items): return sorted(items, reverse=True)
class Sorter:
    def __init__(self, strategy): self.strategy = strategy
    def sort(self, items): return self.strategy(items)

print(Sorter(descending).sort([3, 1, 2]))
