

def deliver_report(destination, report: str) -> None:
    destination.write(report)

class ConsoleDestination:

    def write(self, report: str) -> None:
        print(report)


class FileDestination:

    def write(self, report: str) -> None:
        with open("polymorphism_report.txt", "w", encoding="utf-8") as file:
            file.write(report)

    
report = "Remaining budget: 424.75"

deliver_report(ConsoleDestination(), report)
deliver_report(FileDestination(), report)