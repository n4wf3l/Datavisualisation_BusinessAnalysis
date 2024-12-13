import pandas as pd
import matplotlib.pyplot as plt

# Données ajustées pour les surplus de lundi à dimanche
# Données ajustées pour les surplus de lundi à dimanche
data = {
    'Dag': ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag'],
    'Gehakt': [10, 9, 8, 7, 5, 6, 8],  # Surplus en kg ajustés
    'Gesneden charcuterie': [9, 8, 7, 6, 4, 5, 7],   # Surplus en kg ajustés
    'Gemarineerde kip': [12, 10, 9, 8, 6, 7, 9]     # Surplus en kg ajustés
}

# Prix par kilogramme pour chaque produit
prix_par_kg = {
    'Gehakt': 8,  # Prix en euros par kg
    'Gesneden charcuterie': 12,
    'Gemarineerde kip': 10
}

# Conversion en DataFrame
df_surplus = pd.DataFrame(data).set_index('Dag')

# Calcul du coût total des surplus
df_surplus['Coût (€)'] = (
    df_surplus['Gehakt'] * prix_par_kg['Gehakt'] + 
    df_surplus['Gesneden charcuterie'] * prix_par_kg['Gesneden charcuterie'] + 
    df_surplus['Gemarineerde kip'] * prix_par_kg['Gemarineerde kip']
)

# Création du graphique
fig, ax1 = plt.subplots(figsize=(12, 6))

# Barres pour les surplus
bar_width = 0.25  # Largeur des barres
x = range(len(df_surplus.index))  # Position des barres

# Création des barres groupées
ax1.bar([i - bar_width for i in x], df_surplus['Gehakt'], width=bar_width, label='Gehakt', color='lightblue', alpha=0.6)
ax1.bar(x, df_surplus['Gesneden charcuterie'], width=bar_width, label='Gesneden charcuterie', color='lightgreen', alpha=0.6)
ax1.bar([i + bar_width for i in x], df_surplus['Gemarineerde kip'], width=bar_width, label='Gemarineerde kip', color='lightcoral', alpha=0.6)

# Configuration de l'axe des surplus
ax1.set_ylabel('Overschot (kg)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Ajout des coûts en euros à l'intérieur des barres
for i in x:
    ax1.text(i - bar_width, df_surplus['Gehakt'].iloc[i] / 2, f"{df_surplus['Gehakt'].iloc[i]} kg\n{df_surplus['Gehakt'].iloc[i] * prix_par_kg['Gehakt']} €", ha='center', va='center', color='black')
    ax1.text(i, df_surplus['Gesneden charcuterie'].iloc[i] / 2, f"{df_surplus['Gesneden charcuterie'].iloc[i]} kg\n{df_surplus['Gesneden charcuterie'].iloc[i] * prix_par_kg['Gesneden charcuterie']} €", ha='center', va='center', color='black')
    ax1.text(i + bar_width, df_surplus['Gemarineerde kip'].iloc[i] / 2, f"{df_surplus['Gemarineerde kip'].iloc[i]} kg\n{df_surplus['Gemarineerde kip'].iloc[i] * prix_par_kg['Gemarineerde kip']} €", ha='center', va='center', color='black')

# Configuration du graphique
plt.title('Overschot van Geselecteerde Producten (Maandag tot Zondag)', fontsize=16)
ax1.set_xlabel('Dagen van de week', fontsize=12)
ax1.set_xticks(x)  # Définir les ticks sur l'axe des x
ax1.set_xticklabels(df_surplus.index)  # Étiquettes des jours
fig.tight_layout()

# Ajout de la légende
ax1.legend(loc='upper left')

# Affichage du graphique
plt.show()
