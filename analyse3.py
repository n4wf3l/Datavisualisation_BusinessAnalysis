import matplotlib.pyplot as plt
import numpy as np

# Fictieve gegevens voor het voorbeeld
weken = np.array(['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'])
overschot_van = np.array([50, 40, 30, 20, 10])  # Overschot in kg vóór de promoties
overschot_na = np.array([45, 30, 20, 10, 5])   # Overschot in kg ná de promoties
winst = np.array([200, 300, 400, 600, 800])   # Winst in euro's gegenereerd door de promoties

# Aanmaken van de grafiek voor de impact van de promoties
fig, ax1 = plt.subplots(figsize=(10, 6))

# Balken voor de overschotten
balk_breedte = 0.35
index = np.arange(len(weken))

balk1 = ax1.bar(index, overschot_van, balk_breedte, label='Overschot vóór promoties', color='lightblue')
balk2 = ax1.bar(index + balk_breedte, overschot_na, balk_breedte, label='Overschot ná promoties', color='lightgreen')
ax1.set_ylabel('Hoeveelheid overschot (kg)', color='black')
ax1.set_title("Impact van Promoties op de Overschotten en Winst")
ax1.set_xticks(index + balk_breedte / 2)
ax1.set_xticklabels(weken)
ax1.tick_params(axis='y', labelcolor='black')

# Waarden boven de balken toevoegen
for i in range(len(overschot_van)):
    ax1.text(i, overschot_van[i] + 1, str(overschot_van[i]), ha='center', color='black')
    ax1.text(i + balk_breedte, overschot_na[i] + 1, str(overschot_na[i]), ha='center', color='black')

# Tweede as toevoegen voor de winst
ax2 = ax1.twinx()
ax2.plot(weken, winst, color='orange', marker='o', label='Winst (in €)', linewidth=2)
ax2.set_ylabel('Winst (in €)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Waarden van de winst toevoegen
for i in range(len(winst)):
    ax2.text(i, winst[i] + 20, str(winst[i]), ha='center', color='orange')

# Legenda
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Grafiek weergeven
plt.show()
