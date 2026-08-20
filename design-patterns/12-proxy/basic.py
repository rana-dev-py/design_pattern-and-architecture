"""Virtual proxy loads an expensive value only when needed."""
class Image:
    def __init__(self, path): print("loading", path); self.path = path
    def show(self): return self.path
class ImageProxy:
    def __init__(self, path): self.path, self._image = path, None
    def show(self):
        self._image = self._image or Image(self.path)
        return self._image.show()

print(ImageProxy("photo.png").show())
