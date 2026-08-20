"""Immutable mementos can use dataclasses."""
from dataclasses import dataclass
@dataclass(frozen=True)
class GameState: level: int; score: int

saved = GameState(2, 100)
print(saved)
