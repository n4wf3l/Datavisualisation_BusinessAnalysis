import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données CSV
df = pd.read_csv('surplus_promoties.csv')

# Réorganiser les données pour avoir deux colonnes distinctes pour avec et sans promotion
df_melted = pd.melt(df, id_vars=['week', 'product'], 
                    value_vars=['overschot_met_promotie', 'overschot_zonder_promotie'], 
                    var_name='Promotie', value_name='Overschotten')

# Créer le graphique à barres groupées avec produit et semaine
g = sns.catplot(data=df_melted, x='week', y='Overschotten', hue='Promotie', col='product', 
                kind='bar', palette=['green', 'red'], ci=None, height=4, aspect=0.75)

# Ajouter les annotations pour chaque barre
for ax in g.axes.flat:
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 8),  # Légère distance par rapport à la barre
                    textcoords = 'offset points')

# Ajuster les titres et étiquettes
g.set_titles("{col_name}")  # Garde uniquement le nom du produit
g.set_axis_labels("Week", "Overschotten (in kg)")
g.fig.suptitle('Impact van Promoties op Overschotten (per week, per product)', fontsize=16)

# Désactiver la légende automatique
g._legend.remove()

# Repositionner la légende manuellement avec les bons labels et centrer au milieu
labels = ['Met Promotie', 'Zonder Promotie']
plt.legend(handles=g._legend_data.values(), labels=labels, loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2, title="Promotie")

# Ajuster l'espace entre le titre et la légende
g.fig.subplots_adjust(top=0.75)

# Ajuster l'espace pour éviter le chevauchement
g.fig.tight_layout(rect=[0, 0, 1, 0.9])

plt.show()
