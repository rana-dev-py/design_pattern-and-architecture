"""A visitor can calculate over heterogeneous nodes."""
class Add:
    def __init__(self, left, right): self.left, self.right = left, right
    def accept(self, visitor): return visitor.visit_add(self)
class Evaluator:
    def visit_add(self, node): return node.left + node.right

print(Add(2, 3).accept(Evaluator()))
