"""Python function decorators add cross-cutting behavior."""
def timed(fn):
    def wrapped(*args):
        print("calling", fn.__name__)
        return fn(*args)
    return wrapped

@timed
def greet(name): return f"Hello {name}"

print(greet("Ada"))
