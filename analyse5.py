import pandas as pd
import matplotlib.pyplot as plt

# Dummydata voor funnel analyse
stappen = ['Gestarte cursussen', '50% cursus voltooid', 'Pagina abonnement bezocht', 'Abonnementen gekocht']
aantallen = [10000, 6500, 3500, 700]  # Aantal gebruikers
percentages = ["+0%", "-35%", "-46%", "-80%"]  # Toegevoegde conversiepercentages

# Funnel grafiek maken
fig, ax = plt.subplots(figsize=(12, 6))
kleuren = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Bar chart genereren met percentages
bars = plt.barh(stappen, aantallen, color=kleuren)

# Waarden en percentages toevoegen aan de balken
for i, bar in enumerate(bars):
    plt.text(bar.get_width() - 300, bar.get_y() + bar.get_height()/2,  
             f"{aantallen[i]}\n{percentages[i]}",
             va='center', ha='center', color='white', fontsize=10, fontweight='bold')

# Titel en labels
plt.title('Funnel Analyse van Gebruikers - Winston Wolfe', fontsize=14)
plt.xlabel('Aantal gebruikers', fontsize=12)
plt.ylabel('Funnel Stappen', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Layout aanpassen en grafiek tonen
plt.tight_layout()
plt.show()