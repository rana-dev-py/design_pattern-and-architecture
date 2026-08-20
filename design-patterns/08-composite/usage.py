"""Composite represents an organization tree."""
class Employee:
    def __init__(self, name): self.name = name
    def names(self): return [self.name]
class Team(Employee):
    def __init__(self, name, *members): super().__init__(name); self.members = members
    def names(self): return [self.name] + sum((m.names() for m in self.members), [])

print(Team("Engineering", Employee("Ada"), Employee("Lin")).names())
