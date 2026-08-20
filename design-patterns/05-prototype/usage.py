"""Objects can expose an explicit clone operation."""
from copy import deepcopy

class Report:
    def __init__(self, title, sections): self.title, self.sections = title, sections
    def clone(self): return deepcopy(self)

draft = Report("Monthly", ["Summary"])
june = draft.clone(); june.sections.append("Revenue")
print(draft.sections, june.sections)
