"""A mapping is a compact strategy registry."""
strategies = {"upper": str.upper, "lower": str.lower}
print(strategies["upper"]("Ada"))
