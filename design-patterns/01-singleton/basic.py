"""Minimal Singleton using __new__."""
class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = False
        return cls._instance

if __name__ == "__main__":
    a, b = Settings(), Settings()
    a.debug = True
    print(a is b, b.debug)
