"""Function adapters are useful for callbacks."""
def legacy_handler(event, context): return f"{event}:{context}"
def web_handler(request): return legacy_handler(request["path"], "web")

print(web_handler({"path": "/health"}))
