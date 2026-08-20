"""Double dispatch selects behavior by element type."""
class Circle:
    def accept(self, visitor): return visitor.visit_circle(self)
class Area:
    def visit_circle(self, circle): return 3.14

print(Circle().accept(Area()))
