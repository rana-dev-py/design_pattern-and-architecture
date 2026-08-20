"""Copy a configured prototype."""
from copy import copy

template = {"color": "blue", "items": []}
first = copy(template)
first["items"] = ["pen"]
print(template, first)
