"""Director applies a repeatable construction recipe."""
class PizzaBuilder:
    def __init__(self): self.parts = []
    def add(self, part): self.parts.append(part); return self
    def build(self): return ", ".join(self.parts)

def margherita(builder):
    return builder.add("dough").add("tomato").add("mozzarella").build()

print(margherita(PizzaBuilder()))
