"""UI groups can render children uniformly."""
class Text:
    def render(self): return "text"
class Panel:
    def __init__(self, *children): self.children = children
    def render(self): return "[" + ", ".join(c.render() for c in self.children) + "]"

print(Panel(Text(), Panel(Text())).render())
