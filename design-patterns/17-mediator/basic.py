"""Mediator coordinates colleagues."""
class ChatRoom:
    def send(self, sender, message): print(f"{sender.name}: {message}")
class User:
    def __init__(self, name, room): self.name, self.room = name, room
    def say(self, message): self.room.send(self, message)

User("Ada", ChatRoom()).say("Hello")
