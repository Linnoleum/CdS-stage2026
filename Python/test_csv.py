import csv

with open("cds_autographe.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter="\t")

    id = []
    for row in reader:
        id.append(row["ID"])

print("ID:", id)
