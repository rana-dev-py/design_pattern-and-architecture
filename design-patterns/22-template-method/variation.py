"""Hooks customize optional portions of a workflow."""
class Importer:
    def run(self, text): return self.transform(self.parse(text))
    def parse(self, text): return text.split(",")
    def transform(self, values): return values
class UpperImporter(Importer):
    def transform(self, values): return [v.upper() for v in values]

print(UpperImporter().run("a,b"))
