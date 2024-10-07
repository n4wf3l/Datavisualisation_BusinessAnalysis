import matplotlib.pyplot as plt

# Data from the table in the provided image
weeks = ["2 weken voor Kerstmis", "Voor Kerstmis", "Week na Kerstmis", "Pasen"]
product_1_sales = [60, 90, 50, 70]
product_2_sales = [45, 60, 38, 50]
product_3_sales = [35, 45, 28, 45]
product_1_increase = [33.33, 100, 11.11, 55.56]
product_2_increase = [12.5, 50, -5, 25]
product_3_increase = [16.67, 50, -6.67, 50]

# Plotting the sales data
plt.figure(figsize=(12, 8))
plt.plot(weeks, product_1_sales, label="Product 1 (Biefstuk)", marker='o', linestyle='-', linewidth=2, color='blue')
plt.plot(weeks, product_2_sales, label="Product 2 (Kipfilet)", marker='o', linestyle='-', linewidth=2, color='orange')
plt.plot(weeks, product_3_sales, label="Product 3 (Varkensworstjes)", marker='o', linestyle='-', linewidth=2, color='green')

# Adding labels, title, and legend in Dutch
plt.xlabel('Week', fontsize=12)
plt.ylabel('Verkoop in kg', fontsize=12)
plt.title('Verkoop van Producten tijdens Feestdagen', fontsize=14)
plt.legend()
plt.grid(True)

# Adding annotations to highlight the percentage increase
for i, week in enumerate(weeks):
    plt.annotate(f'+{product_1_increase[i]}%', (week, product_1_sales[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='blue', fontsize=10)
    plt.annotate(f'+{product_2_increase[i]}%', (week, product_2_sales[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='orange', fontsize=10)
    plt.annotate(f'+{product_3_increase[i]}%', (week, product_3_sales[i]), textcoords="offset points", xytext=(0, 10), ha='center', color='green', fontsize=10)

# Adding an average line for comparison
avg_sales = [sum(product_1_sales)/len(product_1_sales), sum(product_2_sales)/len(product_2_sales), sum(product_3_sales)/len(product_3_sales)]
plt.axhline(y=avg_sales[0], color='blue', linestyle='--', linewidth=1, label='Gemiddelde Product 1')
plt.axhline(y=avg_sales[1], color='orange', linestyle='--', linewidth=1, label='Gemiddelde Product 2')
plt.axhline(y=avg_sales[2], color='green', linestyle='--', linewidth=1, label='Gemiddelde Product 3')

plt.tight_layout()

# Show the plot
plt.show()
