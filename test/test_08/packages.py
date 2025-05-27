class Package:

    def __init__(self, number, sender, recipient, wight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.wight = wight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.wight}kg"

    def calculate_cost(self, cost_per_kg):
        return self.wight * cost_per_kg



def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", wight=5),
        Package(number=2, sender="Bob", recipient="Charlie", wight=10)
    ]

    for package in packages:
        print(f"{package} costs ${package.calculate_cost(2)}")


main()
