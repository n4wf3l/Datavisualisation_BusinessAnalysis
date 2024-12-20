import matplotlib.pyplot as plt

# Dummydata: Stappen en hun omzet
stappen = ['Huidige Omzet', 'Klikgedrag bij Call-to-Action', 'Afhaakgedrag na Module 1', 'Conversie bij Proefabonnement']
omzet_groei = [70000, 80000, 95000, 115000] # Cumulatieve groei zonder totaal

# Bepaal de cumulatieve omzet per stap
cumulatieve_waarden = [omzet_groei[0]]  # Beginwaarde
for i in range(1, len(omzet_groei)):
    cumulatieve_waarden.append(cumulatieve_waarden[-1] + omzet_groei[i])

# Kleuren bepalen: huidige en tussenstappen
kleuren = ['lightgray'] + ['skyblue'] * (len(stappen) - 1)

# Maak het kolomdiagram
plt.figure(figsize=(10, 6))
plt.bar(stappen, cumulatieve_waarden, color=kleuren, edgecolor='black')

# Waarden boven de kolommen toevoegen
for i, waarde in enumerate(cumulatieve_waarden):
    plt.text(i, waarde + 2000, f"€{waarde:,}", ha='center', va='bottom', fontsize=10)

# Grafiektitel en labels
plt.title('Cumulatieve Omzetgroei door Data-Analyse', fontsize=14)
plt.ylabel('Cumulatieve Omzet (€)', fontsize=12)
plt.xticks(rotation=15, fontsize=10)
plt.yticks(fontsize=10)

# Netjes gridlijnen toevoegen
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Layout optimaliseren en grafiek tonen
plt.tight_layout()
plt.show()
