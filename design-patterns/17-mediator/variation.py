"""Form mediator centralizes UI rules."""
class LoginForm:
    def submit(self, username, password):
        return "accepted" if username and len(password) >= 8 else "invalid"

print(LoginForm().submit("ada", "long-password"))
