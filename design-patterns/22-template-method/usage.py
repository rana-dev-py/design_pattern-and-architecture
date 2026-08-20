"""Framework callbacks are template-method style."""
class TestCase:
    def run(self): self.set_up(); result = self.test(); self.tear_down(); return result
    def set_up(self): pass
    def tear_down(self): pass
    def test(self): return "passed"

print(TestCase().run())
