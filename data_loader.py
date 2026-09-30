import csv

# laddar in patientdata från CSV-filen
def load_data(file_name):
    with open(file_name, 'r', encoding= 'utf-8') as file:
        reader = csv.DictReader(file)
        rows = []

        for row in reader:
            rows.append(row)
    return rows