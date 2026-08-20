"""Generators are concise Python iterators."""
def chunks(items, size):
    for index in range(0, len(items), size):
        yield items[index:index + size]

print(list(chunks([1, 2, 3, 4, 5], 2)))
