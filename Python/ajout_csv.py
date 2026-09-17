import csv
import re

cotes = {}  # On initialise un dictionnaire vide qui accueillera les cotes correspondantes


with open("abschrift_cds.txt", encoding="utf-8") as file:
    for ligne in file:
        match = re.match(r"(\d+).*?\['([^']+)'", ligne)

        if match:
            id = match.group(1)
            cote = match.group(2)
            cotes[id] = (
                cote  # On récupère les cotes contenues dans le fichier texte ouvert à l'occasion
            )


with open("cds_autographe.csv", encoding="utf-8-sig") as file:
    documents = list(csv.DictReader(file, delimiter="\t"))  # On lit le fichier CSV


for document in documents:
    document["Cote"] = cotes.get(
        document["ID"], ""
    )  # On ajoute la cote que l'on cherche au dictionnaire avec son identifiant retrouvé dans le fichier CSV correspondant


with open("cds_corr_cotes.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=documents[0].keys(), delimiter="\t")

    writer.writeheader()
    writer.writerows(
        documents
    )  # On écrit ces cotes dans une nouvelle colonne du fichier CSV
