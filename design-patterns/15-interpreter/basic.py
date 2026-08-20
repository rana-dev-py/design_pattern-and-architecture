"""Expression objects interpret a tiny boolean language."""
class Equals:
    def __init__(self, key, value): self.key, self.value = key, value
    def interpret(self, context): return context.get(self.key) == self.value

print(Equals("role", "admin").interpret({"role": "admin"}))
