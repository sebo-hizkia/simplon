import csv # module standard de Python pour lire/écrire des fichiers CSV
import urllib.request # module standard pour télécharger du contenu depuis une URL

# Télécharger et lire le jeu de données
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv"
response = urllib.request.urlopen(url) # Ouvre une connexion HTTP vers l’URL donnée.
lines = [l.decode("utf-8") for l in response.readlines()] # Lit toutes les lignes de la réponse HTTP (données brutes encodées) et les décodes
reader = csv.DictReader(lines) # Lit les données CSV ligne par ligne et les transforme en dictionnaires

# Initialiser un dictionnaire vide pour stocker le cumul des quantités par produit
ventes_par_produit = {}

# Calculer et stocker les quantités totales par produit
for row in reader:
    produit = row["produit"]
    qte = int(row["qte"])
    ventes_par_produit[produit] = ventes_par_produit.get(produit, 0) + qte

# Trouver le produit le plus et le moins vendu
produit_plus_vendu = max(ventes_par_produit, key=ventes_par_produit.get)
produit_moins_vendu = min(ventes_par_produit, key=ventes_par_produit.get)

print("Quantités vendues par produit :", ventes_par_produit)
print("Produit le plus vendu :", produit_plus_vendu, "→", ventes_par_produit[produit_plus_vendu], "unités")
print("Produit le moins vendu :", produit_moins_vendu, "→", ventes_par_produit[produit_moins_vendu], "unités")
