"""Switching factories switches a whole product family."""
class MacButton:
    def draw(self): return "mac button"
class WindowsButton:
    def draw(self): return "windows button"

class GUIFactory:
    def __init__(self, platform): self.platform = platform
    def button(self):
        return MacButton() if self.platform == "mac" else WindowsButton()

print(GUIFactory("windows").button().draw())
