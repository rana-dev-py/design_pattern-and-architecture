"""Facade gives an application-focused API."""
class Database:
    def save(self, user): return user
class UserService:
    def register(self, name): return Database().save({"name": name})

print(UserService().register("Ada"))
