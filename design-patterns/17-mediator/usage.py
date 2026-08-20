"""Air traffic control is another mediator example."""
class Tower:
    def request_landing(self, plane): return f"{plane} cleared to land"

print(Tower().request_landing("Flight 42"))
