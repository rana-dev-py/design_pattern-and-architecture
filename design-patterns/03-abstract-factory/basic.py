"""Factory creates compatible light-theme widgets."""
class LightButton:
    def draw(self): return "light button"
class LightMenu:
    def draw(self): return "light menu"

class LightTheme:
    def button(self): return LightButton()
    def menu(self): return LightMenu()

theme = LightTheme()
print(theme.button().draw(), theme.menu().draw())
