import pandas as pd
import matplotlib.pyplot as plt

# Lire les données à partir du fichier CSV
csv_file_path = "feast_sales_data.csv"
df = pd.read_csv(csv_file_path)

# Extraire les données du DataFrame
weeks = df["Week"].tolist()
product_1_sales = df["Product 1 Sales"].tolist()
product_2_sales = df["Product 2 Sales"].tolist()
product_3_sales = df["Product 3 Sales"].tolist()
product_1_increase = df["Product 1 Increase"].tolist()
product_2_increase = df["Product 2 Increase"].tolist()
product_3_increase = df["Product 3 Increase"].tolist()

# Tracer les données de vente
plt.figure(figsize=(12, 8))
plt.plot(weeks, product_1_sales, label="Product 1 (Biefstuk)", marker='o', linestyle='-', linewidth=2, color='blue')
plt.plot(weeks, product_2_sales, label="Product 2 (Kipfilet)", marker='o', linestyle='-', linewidth=2, color='orange')
plt.plot(weeks, product_3_sales, label="Product 3 (Varkensworstjes)", marker='o', linestyle='-', linewidth=2, color='green')

# Ajouter des étiquettes, un titre et une légende en néerlandais
plt.xlabel('Week', fontsize=12)
plt.ylabel('Verkoop in kg', fontsize=12)
plt.title('Verkoop van Producten tijdens Feestdagen', fontsize=14)
plt.legend()
plt.grid(True)

# Ajouter des annotations pour mettre en évidence le pourcentage d'augmentation
for i, week in enumerate(weeks):
    plt.annotate(f'+{product_1_increase[i]}%', (week, product_1_sales[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue', fontsize=10)
    plt.annotate(f'+{product_2_increase[i]}%', (week, product_2_sales[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='orange', fontsize=10)
    plt.annotate(f'+{product_3_increase[i]}%', (week, product_3_sales[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='green', fontsize=10)

# Ajouter une ligne moyenne pour comparaison
avg_sales = [sum(product_1_sales)/len(product_1_sales), sum(product_2_sales)/len(product_2_sales), sum(product_3_sales)/len(product_3_sales)]
plt.axhline(y=avg_sales[0], color='blue', linestyle='--', linewidth=1, label='Gemiddelde Product 1')
plt.axhline(y=avg_sales[1], color='orange', linestyle='--', linewidth=1, label='Gemiddelde Product 2')
plt.axhline(y=avg_sales[2], color='green', linestyle='--', linewidth=1, label='Gemiddelde Product 3')

plt.tight_layout()

# Afficher le graphique
plt.show()
