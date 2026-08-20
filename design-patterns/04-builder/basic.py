"""Fluent builder for an HTTP request."""
class RequestBuilder:
    def __init__(self): self.request = {"headers": {}}
    def url(self, value): self.request["url"] = value; return self
    def header(self, key, value): self.request["headers"][key] = value; return self
    def build(self): return self.request

print(RequestBuilder().url("/users").header("Accept", "json").build())
