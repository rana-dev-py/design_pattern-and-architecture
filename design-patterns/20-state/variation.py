"""Order behavior depends on its current state."""
class Order:
    def __init__(self): self.state = "new"
    def pay(self):
        if self.state != "new": raise ValueError("cannot pay")
        self.state = "paid"

order = Order(); order.pay(); print(order.state)
