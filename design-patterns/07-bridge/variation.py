"""Shapes and renderers vary independently."""
class SvgRenderer:
    def render_circle(self, radius): return f"<circle r='{radius}' />"
class Circle:
    def __init__(self, renderer, radius): self.renderer, self.radius = renderer, radius
    def draw(self): return self.renderer.render_circle(self.radius)

print(Circle(SvgRenderer(), 5).draw())
