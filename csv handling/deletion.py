import csv

csv_file = 'organizations.csv'
indexes_to_delete = [10, 12, 15]
with open(csv_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
     
    orgs = [org for org in reader if int(org['Index']) not in indexes_to_delete]

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(orgs)