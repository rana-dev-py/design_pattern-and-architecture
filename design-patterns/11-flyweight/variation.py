"""Trees share species data; position stays external."""
class TreeType:
    def __init__(self, name, color): self.name, self.color = name, color
class Tree:
    def __init__(self, tree_type, x, y): self.tree_type, self.x, self.y = tree_type, x, y

oak = TreeType("oak", "green")
forest = [Tree(oak, 1, 2), Tree(oak, 3, 4)]
print(forest[0].tree_type is forest[1].tree_type)
