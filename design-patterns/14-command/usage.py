"""Invoker queues commands without knowing their details."""
class Print:
    def __init__(self, text): self.text = text
    def execute(self): print(self.text)

queue = [Print("first"), Print("second")]
for command in queue: command.execute()
