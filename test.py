import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('./datasets/dataset_test.csv')

# Sélection des colonnes numériques uniquement
numerical_cols = df.select_dtypes(include=['number']).columns


# Normalisation des données

# Création de l'histogramme
# plt.figure(figsize=(8, 6))
#
# # Sélectionner trois features aléatoirement (ou définir manuellement)
# features = data.columns[:3]
#
# colors = ['blue', 'green', 'red']
# for feature, color in zip(features, colors):
#     plt.hist(data[feature], bins=30, alpha=0.5, color=color, label=feature)
#
# # Personnalisation du graphique
# plt.xlabel('Valeurs normalisées')
# plt.ylabel('Fréquence')
# plt.legend()
# plt.show()

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Génération de données aléatoires
# np.random.seed(42)
# data = pd.DataFrame({
#     'Feature 1': np.random.normal(loc=1, scale=1, size=1000),
#     'Feature 2': np.random.normal(loc=0, scale=1, size=1000),
#     'Feature 3': np.random.normal(loc=-1, scale=1, size=1000)
# })
#
# # Création de l'histogramme
# plt.figure(figsize=(8, 6))
# plt.hist(data['Feature 1'], bins=30, alpha=0.5, color='blue', label='Feature 1')
# plt.hist(data['Feature 2'], bins=30, alpha=0.5, color='green', label='Feature 2')
# plt.hist(data['Feature 3'], bins=30, alpha=0.5, color='red', label='Feature 3')
#
# # Personnalisation
# plt.xlabel('Valeurs')
# plt.ylabel('Fréquence')
# plt.legend()
# plt.show()
