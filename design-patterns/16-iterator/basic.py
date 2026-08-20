"""Custom iterable implements __iter__."""
class Countdown:
    def __init__(self, start): self.start = start
    def __iter__(self):
        for value in range(self.start, 0, -1):
            yield value

print(list(Countdown(3)))
