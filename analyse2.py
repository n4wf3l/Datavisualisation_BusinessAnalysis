import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_file_path = "overschotten_per_dag.csv"
df = pd.read_csv(csv_file_path)

jours = df["Dag"]
overschotten_kip = df["Kippenborst (Overschotten)"]
overschotten_rund = df["Rundvlees (Overschotten)"]
overschotten_varken = df["Varkensworstjes (Overschotten)"]

x = np.arange(len(jours))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width, overschotten_kip, width, label="Kippenborst (Overschotten)", color='skyblue')
bars2 = ax.bar(x, overschotten_rund, width, label="Rundvlees (Overschotten)", color='orange')
bars3 = ax.bar(x + width, overschotten_varken, width, label="Varkensworstjes (Overschotten)", color='lightgreen')

for bars in [bars1, bars2, bars3]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'{yval} kg', ha='center', va='bottom', fontsize=10)

ax.set_xlabel('Dag van de Week', fontsize=12)
ax.set_ylabel('Aantal Overschotten (kg)', fontsize=12)
ax.set_title('Analyse van Overschotten per Dag van de Week en per Product', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(jours)
ax.legend()

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()
