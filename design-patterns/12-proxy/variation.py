"""Protection proxy checks access before delegation."""
class Secret:
    def read(self): return "classified"
class Guard:
    def __init__(self, user): self.user = user
    def read(self):
        if self.user != "admin": raise PermissionError("forbidden")
        return Secret().read()

print(Guard("admin").read())
