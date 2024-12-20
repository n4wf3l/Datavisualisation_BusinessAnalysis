import pandas as pd
import matplotlib.pyplot as plt

# Dummydata voor voor-en-na resultaten van conversietests
data = {
    'Oplossing': ['Call-to-Action Test', 'Introductie Test', 'Proefabonnement Test'],
    'Conversie Voor (%)': [7, 7, 7],  # Huidige conversie voor de tests
    'Conversie Na (%)': [8, 9, 10]    # Resultaten na de tests
}

# DataFrame maken
df_conversie = pd.DataFrame(data)

# Positie van de balken bepalen
x = range(len(df_conversie['Oplossing']))
bar_width = 0.35

# Grafiek maken
plt.figure(figsize=(10, 6))
plt.bar([i - bar_width/2 for i in x], df_conversie['Conversie Voor (%)'], width=bar_width, label='Voor', color='lightgray')
plt.bar([i + bar_width/2 for i in x], df_conversie['Conversie Na (%)'], width=bar_width, label='Na', color='lightblue')

# Titels en labels
plt.title('Voor- en na-resultaten van conversietests', fontsize=14)
plt.ylabel('Conversiepercentage (%)', fontsize=12)
plt.xticks(x, df_conversie['Oplossing'], rotation=15)
plt.xlabel('Oplossingen', fontsize=12)
plt.legend()

# Waarden boven de balken tonen
for i, (v1, v2) in enumerate(zip(df_conversie['Conversie Voor (%)'], df_conversie['Conversie Na (%)'])):
    plt.text(i - bar_width/2, v1 + 0.2, f"{v1}%", ha='center', va='bottom', fontsize=10)
    plt.text(i + bar_width/2, v2 + 0.2, f"{v2}%", ha='center', va='bottom', fontsize=10)

# Layout aanpassen en grafiek tonen
plt.tight_layout()
plt.show()
