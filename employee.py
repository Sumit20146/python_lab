import json

with open("employee.json", "r") as f:
    data = json.load(f)

amount = int(input("Enter salary: "))

for e in data:
    if e["salary"] > amount:
        print(e)