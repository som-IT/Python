import csv

new_org = {
    'Index': 101,
    'Organization Id': 'gger4345df',
    'Name': 'New Organization',
    'Website': 'https://www.neworganization.com',
    'Country': 'USA',
    'Founded': 2024,
    'Description': 'A leading technology solutions provider',
    'Industry': 'Technology',
    'Number of employees': 500
}

csv_file = 'organizations.csv'

with open(csv_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    
if all(field in new_org for field in fieldnames):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_org)
    print(f"New Organization was added to {csv_file}" )
else:
    print("New organization does not have all required fields and was not added!")