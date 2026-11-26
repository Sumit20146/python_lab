class Resident:
    def __init__(self, name, flat, fee, status):
        self.name = name
        self.flat = flat
        self.fee = fee
        self.status = status

    def display(self):
        print(self.name, self.flat, self.fee, self.status)


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self, r):
        self.residents.append(r)

    def display_all(self):
        for r in self.residents:
            r.display()


s = Society()

n = int(input("Enter number of residents: "))

for i in range(n):
    name = input("Enter name: ")
    flat = input("Enter flat number: ")
    fee = int(input("Enter maintenance fee: "))
    status = input("Enter status (Paid/Pending): ")

    r = Resident(name, flat, fee, status)
    s.add_resident(r)

print("\nMaintenance Details:")
s.display_all()
