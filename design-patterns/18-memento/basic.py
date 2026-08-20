"""Memento stores state for undo."""
class Editor:
    def __init__(self): self.text = ""
    def save(self): return self.text
    def restore(self, snapshot): self.text = snapshot

editor = Editor(); editor.text = "draft"; saved = editor.save(); editor.text = "changed"; editor.restore(saved); print(editor.text)
