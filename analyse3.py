import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_file_path = "opslagtijd_per_product.csv"
df = pd.read_csv(csv_file_path)

producten = df["Product"].unique()
opslagtijd = [df[df["Product"] == product]["Opslagtijd"].tolist() for product in producten]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(opslagtijd, labels=producten, patch_artist=True)

ax.set_title('Analyse van de Opslagtijd per Product en Invloed op Overschotten', fontsize=14)
ax.set_xlabel('Product', fontsize=12)
ax.set_ylabel('Opslagtijd (dagen)', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

colors = ['skyblue', 'orange', 'lightgreen']
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

plt.tight_layout()

plt.show()
