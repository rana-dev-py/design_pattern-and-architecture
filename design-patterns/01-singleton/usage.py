"""Thread-safe Singleton."""
from threading import Lock

class ConnectionPool:
    _instance, _lock = None, Lock()
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

print(ConnectionPool() is ConnectionPool())
