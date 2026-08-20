"""A video facade exposes one simple method."""
class Codec:
    def decode(self, path): return f"frames from {path}"
class VideoConverter:
    def to_gif(self, path): return Codec().decode(path) + " -> gif"

print(VideoConverter().to_gif("demo.mp4"))
