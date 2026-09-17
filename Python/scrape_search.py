import csv

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with open("cds_corr_cotes.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter="\t")

    cotes = []

    for row in reader:
        if row["Cote"]:
            cotes.append(row["Cote"]) #On ajoute les cotes trouvées dans le fichier CSV dans notre liste


driver = webdriver.Chrome() #On utilise le navigateur chrome


for cote in cotes:
    print("\nRecherche :", cote)

    driver.get("https://www.constance-de-salm.de/archiv/#/search") #On consulte l'url

    try:
        bouton = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'J’accepte')]"))
        )

        bouton.click() #On ferme la bannière de cookies

    except TimeoutException:
        pass

    recherche = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@placeholder='Saisissez un terme de recherche']")
        )
    ) #On trouve la barre de recherche

    recherche.click()
    recherche.send_keys(cote)
    recherche.send_keys("\n") #On tape la cote dans la barre de recherche et on envoie la requête

    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), cote)
        ) #On attend que le contenu de la page charge

    except TimeoutException:
        print("Résultat non trouvé :", cote)
        continue

    resultats = driver.find_elements(
        By.XPATH, f"//a[.//*[normalize-space(text())='{cote}']]"
    )

    if len(resultats) == 0:
        print("Document introuvable :", cote)
        continue

    print("Document trouvé :", cote) #Le code renvoie le document qui correspond précisément à la cote recherchée

    driver.execute_script("arguments[0].click();", resultats[0]) #On clique sur le document

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/vimg/"]'))
        ) #On attend que les liens des images chargent sur la page

    except TimeoutException:
        print("Images non trouvées :", cote)
        continue

    liens = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/vimg/"]')

    print(len(liens), "image(s) trouvée(s)")

    for i, lien in enumerate(liens, start=1):
        url = lien.get_attribute("href")

        if url:
            nom = cote.replace("/", "_") + "_" + str(i) + ".jpg"

            print("  →", nom)

            image = requests.get(url)

            with open(f"images/{nom}", "wb") as f:
                f.write(image.content) #On télécharge les images et on les associe à leur nom

driver.quit()
