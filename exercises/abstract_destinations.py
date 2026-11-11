from abc import ABC, abstractmethod

class ReportDestination(ABC):
    @abstractmethod
    def write(self, report: str) -> None:
        pass


class ConsoleDestination(ReportDestination):
    def write(self, report: str) -> None:
        print(report)

destination = ConsoleDestination()
destination.write("MyBudget report")

