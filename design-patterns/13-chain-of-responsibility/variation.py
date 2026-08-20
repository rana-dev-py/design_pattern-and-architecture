"""Validation chain stops at the first failure."""
def required(value): return "required" if not value else None
def long_enough(value): return "too short" if len(value) < 3 else None
def validate(value):
    return next((error for rule in (required, long_enough) if (error := rule(value))), "valid")

print(validate("Ada"))
