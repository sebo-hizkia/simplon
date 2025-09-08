import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

# figure.write_html('ventes-par-region.html')

# print('ventes-par-région.html généré avec succès !')

# Ajout de la colonne "CA" (Chiffre d’Affaires) au jeu de données
données["CA"] = données["prix"] * données["qte"]
# print(données)

# CA ventes par produit
ca_produit = données.groupby("produit")["CA"]
print("CA ventes par produit", ca_produit.sum())

# Moyenne et médiane du CA par produit
print("Moyenne des ventes par produit", ca_produit.mean())
print("Mediane des ventes par produit",ca_produit.median())

# Volume ventes par produit
volume_produit = données.groupby("produit")["qte"]
print("Volume des ventes par produit", volume_produit.sum())

# Moyenne et médiane du volume par produit
print("Moyenne", volume_produit.mean())
print("Mediane", volume_produit.median())

# Ecart-type et variance du volume par produit
print("Ecart-type", volume_produit.std())
print("Variance", volume_produit.var())

# print(volume_produit)

# Graphiques
figure = px.pie(données.groupby("produit").sum().reset_index(), values='qte', names='produit', title='volume par produit')
figure.write_html('ventes-par-produit.html')

figure = px.pie(données.groupby("produit").sum().reset_index(), values='CA', names='produit', title='CA par produit')
figure.write_html('ca-par-produit.html')

#print('ventes-par-produit.html généré avec succès !')
