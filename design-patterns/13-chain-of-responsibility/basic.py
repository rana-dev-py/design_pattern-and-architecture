"""Handlers either process or pass on a request."""
class Handler:
    def __init__(self, next_handler=None): self.next = next_handler
    def handle(self, request):
        return self.next.handle(request) if self.next else "unhandled"
class Auth(Handler):
    def handle(self, request):
        return super().handle(request) if request != "login" else "authenticated"

print(Auth(Handler()).handle("login"))
