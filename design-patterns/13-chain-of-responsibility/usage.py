"""Middleware is a common chain-of-responsibility form."""
def logging(next_step): return lambda request: (print(request), next_step(request))[1]
def endpoint(request): return {"status": 200, "path": request["path"]}

print(logging(endpoint)({"path": "/"}))
