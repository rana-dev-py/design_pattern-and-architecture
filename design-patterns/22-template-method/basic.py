"""Base class fixes an algorithm and subclasses fill steps."""
from abc import ABC, abstractmethod
class Report(ABC):
    def render(self): return self.header() + "\n" + self.body()
    def header(self): return "Report"
    @abstractmethod
    def body(self): pass
class SalesReport(Report):
    def body(self): return "Sales: 100"

print(SalesReport().render())
