"""Enum states can model a small finite workflow."""
from enum import Enum
class Status(Enum): DRAFT = 1; PUBLISHED = 2
status = Status.DRAFT
status = Status.PUBLISHED
print(status.name)
