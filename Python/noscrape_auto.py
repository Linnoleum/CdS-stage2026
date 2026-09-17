import csv
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

id = []

with open("cds_autographe.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter="\t")

    for row in reader:
        id.append(row["ID"])

driver = webdriver.Chrome()

for identifiant in id:
    driver.get(f"https://www.constance-de-salm.de/archiv/#/document/{identifiant}")

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Métadonnées")
    )

    texte = driver.find_element(By.TAG_NAME, "body").text

    references = re.findall(r"Abschrift:\s*([^;\n]+)", texte)

    print(identifiant, references)

driver.quit()
