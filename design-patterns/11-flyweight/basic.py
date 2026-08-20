"""Share intrinsic state between many objects."""
class Glyph:
    _cache = {}
    def __new__(cls, char):
        if char not in cls._cache:
            obj = super().__new__(cls); obj.char = char; cls._cache[char] = obj
        return cls._cache[char]

print(Glyph("a") is Glyph("a"))
