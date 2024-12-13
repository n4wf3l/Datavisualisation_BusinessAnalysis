import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Chemin du fichier CSV
csv_file_path = "overschotten_per_dag.csv"

# Lecture du fichier CSV
df = pd.read_csv(csv_file_path)

# Noms des colonnes correspondant aux jours et produits
jours = df["Dag"]
overschotten_bloedworst = df["Gehakt (Overschotten)"]
overschotten_charcuterie = df["Gesneden charcuterie (Overschotten)"]
overschotten_kip = df["Gemarineerde kip (Overschotten)"]

# Création de l'axe X pour les jours de la semaine
x = np.arange(len(jours))
width = 0.25

# Création de la figure et des sous-graphiques
fig, ax = plt.subplots(figsize=(10, 6))

# Création des barres pour chaque produit
bars1 = ax.bar(x - width, overschotten_bloedworst, width, label="Gehakt (Overschotten)", color='skyblue')
bars2 = ax.bar(x, overschotten_charcuterie, width, label="Gesneden charcuterie (Overschotten)", color='orange')
bars3 = ax.bar(x + width, overschotten_kip, width, label="Gemarineerde kip (Overschotten)", color='lightgreen')

# Ajout des annotations sur les barres
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'{yval} kg', ha='center', va='bottom', fontsize=10)

# Ajout des étiquettes et du titre
ax.set_xlabel('Dag van de Week', fontsize=12)
ax.set_ylabel('Aantal Overschotten (kg)', fontsize=12)
ax.set_title('Analyse van Overschotten per Dag van de Week en per Product', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(jours)
ax.legend()

# Ajout de la grille
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustement du layout
plt.tight_layout()

# Affichage du graphique
plt.show()
