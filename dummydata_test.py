import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

np.random.seed(42)
sans_promotion = np.random.normal(loc=20, scale=5, size=30)

avec_promotion = np.random.normal(loc=12, scale=4, size=30)

plt.figure(figsize=(10, 6))
plt.hist(sans_promotion, bins=10, alpha=0.7, label='Zonder Promotie', color='skyblue')
plt.hist(avec_promotion, bins=10, alpha=0.7, label='Met Promotie', color='orange')
plt.xlabel('Aantal Overschotten (kg)')
plt.ylabel('Frequentie')
plt.title('Vergelijking van Overschotten met en zonder Promotie')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

t_stat, p_value = stats.ttest_ind(sans_promotion, avec_promotion)

alpha = 0.05
if p_value < alpha:
    conclusion = "We verwerpen de nulhypothese: de promotie heeft een significant effect op het verminderen van overschotten."
else:
    conclusion = "We kunnen de nulhypothese niet verwerpen: er is geen significant effect van de promotie op het verminderen van overschotten."

print(f"t-statistiek: {t_stat}")
print(f"p-waarde: {p_value}")
print(conclusion)
