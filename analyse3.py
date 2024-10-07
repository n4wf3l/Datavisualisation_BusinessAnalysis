import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lire les données à partir du fichier CSV renommé
csv_file_path = "opslagtijd_per_product.csv"  # Assurez-vous que ce chemin correspond à l'emplacement correct
df = pd.read_csv(csv_file_path)

# Extraire les données du DataFrame
producten = df["Product"].unique()
opslagtijd = [df[df["Product"] == product]["Opslagtijd"].tolist() for product in producten]

# Création du graphique en utilisant les données de durée de stockage
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(opslagtijd, labels=producten, patch_artist=True)

# Personnalisation du graphique
ax.set_title('Analyse van de Opslagtijd per Product en Invloed op Overschotten', fontsize=14)
ax.set_xlabel('Product', fontsize=12)
ax.set_ylabel('Opslagtijd (dagen)', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ajouter des couleurs différentes pour chaque boîte
colors = ['skyblue', 'orange', 'lightgreen']
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

# Ajuster la disposition pour éviter le chevauchement
plt.tight_layout()

# Afficher le graphique
plt.show()
