import csv

with open("organizations.csv", mode="r") as file:
    reader = csv.DictReader(file)
    orgs = [row for row in reader]

sw_orgs = [org for org in orgs if org["Country"]=="Sweden"]

with open("sw_orgs.csv", mode="w", newline='') as file:
    fieldnames = sw_orgs[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(sw_orgs)