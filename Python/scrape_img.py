import csv

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

id = [] #On initialise une liste qui accueillera nos identifiants recherchés

with open("cds_autographe.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter="\t") #On lit le fichier CSV

    for row in reader:
        id.append(row["ID"]) #On ajoute l'identifiant du CSV à la liste des identifiants

driver = webdriver.Chrome() #On utilise le navigateur Chrome pour notre scrapping

for identifiant in id:
    driver.get(f"https://www.constance-de-salm.de/archiv/#/document/{identifiant}") #On accède à l'URL du document selon son identifiant dans la liste

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Métadonnées")
    ) #On attend que les éléments de la page chargent, sinon le programme s'interrompt avec une erreur


    liens = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/vimg/"]') #On trouve les liens de téléchargement des images du document sur la page


    for lien in liens:
        url = lien.get_attribute("href")
        if url:
            nom = url.split("/")[-1]

            print(f"{identifiant} → {nom}") #On fait correspondre l'identifiant du document avec le nom attribué

            image = requests.get(url)
            with open(f"images/{nom}", "wb") as f:
                f.write(image.content) #On télécharge l'image

driver.quit() #On ferme le navigateur
