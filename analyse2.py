import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lire les données à partir du fichier CSV généré
csv_file_path = "overschotten_per_dag.csv"
df = pd.read_csv(csv_file_path)

# Extraire les données du DataFrame
jours = df["Dag"]
overschotten_kip = df["Kippenborst (Overschotten)"]
overschotten_rund = df["Rundvlees (Overschotten)"]
overschotten_varken = df["Varkensworstjes (Overschotten)"]

# Positionnement des barres sur l'axe x
x = np.arange(len(jours))
width = 0.25

# Création du graphique
fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width, overschotten_kip, width, label="Kippenborst (Overschotten)", color='skyblue')
bars2 = ax.bar(x, overschotten_rund, width, label="Rundvlees (Overschotten)", color='orange')
bars3 = ax.bar(x + width, overschotten_varken, width, label="Varkensworstjes (Overschotten)", color='lightgreen')

# Ajouter des annotations pour chaque barre
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'{yval} kg', ha='center', va='bottom', fontsize=10)

# Ajouter des étiquettes, un titre et une légende en néerlandais
ax.set_xlabel('Dag van de Week', fontsize=12)
ax.set_ylabel('Aantal Overschotten (kg)', fontsize=12)
ax.set_title('Analyse van Overschotten per Dag van de Week en per Product', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(jours)
ax.legend()

# Ajouter une grille pour améliorer la lisibilité
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ajuster la disposition pour éviter le chevauchement
plt.tight_layout()

# Afficher le graphique
plt.show()
