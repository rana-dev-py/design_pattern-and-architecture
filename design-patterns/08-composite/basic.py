"""Leaves and composites share one operation."""
class File:
    def __init__(self, name): self.name = name
    def size(self): return 1
class Folder:
    def __init__(self, *children): self.children = children
    def size(self): return sum(child.size() for child in self.children)

print(Folder(File("a"), Folder(File("b"))).size())
