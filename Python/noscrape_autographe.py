import csv

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Lire les ID et les cotes
documents = []

with open("cds_corr_cotes.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter="\t")

    for row in reader:
        if row["Cote"]:
            documents.append((row["ID"], row["Cote"]))


driver = webdriver.Chrome()

for identifiant, cote in documents:
    driver.get(f"https://www.constance-de-salm.de/archiv/#/document/{identifiant}")

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Métadonnées")
    )

    # Trouver les liens vers les images
    liens = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/vimg/"]')

    print(identifiant, "→", cote, "→", len(liens), "image(s)")

    # Télécharger les images
    for i, lien in enumerate(liens, start=1):
        url = lien.get_attribute("href")

        if url:
            nom = cote.replace("/", "_") + "_" + str(i) + ".jpg"

            print("  →", nom)

            image = requests.get(url)

            with open(f"images_autographe/{nom}", "wb") as f:
                f.write(image.content)


driver.quit()
