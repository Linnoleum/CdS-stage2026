# Dépôt du stage (été 2026) sur la correspondance de Constance de Salm

Ce dépôt GitHub recense les scripts Python et les fichiers XML produits à l'occasion d'un stage de fin de première année de master TNAH durant l'été 2026.

## Scripts Python
- ```scrape_img.py``` est le script utilisé pour télécharger automatiquement les images présentes sur la page d'un document dont on a donné l'identifiant au préalable à partir du fichier CSV ```cds_autographe.csv```.
- ```scrape_search.py``` permet de rechercher un document à partir de sa cote, extraite depuis ```cs_corr_cotes.csv```, dans l'outil de recherche proposé sur le site de la collection, puis de télécharger les images nécessaires.
- ```ajout_csv.py``` nous permet d'ajouter les cotes extraites du fichier ```abschrift_cds.txt``` dans une nouvelle colonne du fichier CSV ```cds_autographe.csv```.
- ```autographe_results.txt``` nous renvoie le résultat de notre collecte d'images.
- Les dossiers ```images``` et ```images_autographes``` contiennent les images des lettres rédigées par les secrétaires et les images de ces mêmes lettres écrites de la main de Constance de Salm.

## XML
- Le fichier ```2026_model_edition_cds.xml``` correspond au modèle-type utilisé pour éditer une lettre en XML-TEI, et le fichier ```lettre_constant``` est un exemple de lettre éditée à partir de ce modèle.
