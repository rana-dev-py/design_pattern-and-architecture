"""A small command interpreter maps words to actions."""
commands = {"start": lambda: "started", "stop": lambda: "stopped"}
def interpret(text): return commands.get(text, lambda: "unknown")()

print(interpret("start"))
