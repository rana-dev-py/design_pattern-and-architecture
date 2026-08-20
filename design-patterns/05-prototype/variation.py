"""Deep copy preserves independent nested state."""
from copy import deepcopy

original = {"position": [0, 0], "style": {"font": "sans"}}
clone = deepcopy(original)
clone["position"][0] = 10
print(original["position"], clone["position"])
