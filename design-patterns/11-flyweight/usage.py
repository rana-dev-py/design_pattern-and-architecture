"""Interning repeated values is a flyweight-like optimization."""
from sys import intern

first, second = intern("active"), intern("active")
print(first is second)
