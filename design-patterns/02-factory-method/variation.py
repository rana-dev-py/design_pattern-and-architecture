"""A document factory selects the parser."""
class JsonParser:
    def parse(self, text): return {"format": "json", "text": text}

class ParserFactory:
    @staticmethod
    def create(extension):
        if extension == ".json":
            return JsonParser()
        raise ValueError("unsupported format")

print(ParserFactory.create(".json").parse("{}"))
