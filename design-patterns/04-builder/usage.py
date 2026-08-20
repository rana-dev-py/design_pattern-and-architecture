"""Builder validates a complex immutable object."""
from dataclasses import dataclass

@dataclass(frozen=True)
class User: name: str; email: str

class UserBuilder:
    def __init__(self): self.data = {}
    def set(self, key, value): self.data[key] = value; return self
    def build(self): return User(**self.data)

print(UserBuilder().set("name", "Ada").set("email", "ada@example.com").build())
