import pandas as pd
from utils import au_25, au_50, au_75, au_max, au_mean, au_min, au_std

df = pd.read_csv('./datasets/dataset_test.csv')
pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)

# Initialiser un dictionnaire pour stocker les statistiques
stats = {
    "count": [],
    "Mean": [],
    "Std": [],
    "Min": [],
    "25%": [],
    "50%": [],
    "75%": [],
    "Max": [],
}


columns = []  # Liste des noms des colonnes retenues

# Itération sur les colonnes
for series_name, series in df.items():
    if series_name not in ["Index", "Hogwarts House", "First Name",
                           "Last Name", "Birthday", "Best Hand"]:
        columns.append(series_name)  # Ajouter le nom de la colonne

        stats["count"].append(series.count())

        if pd.api.types.is_numeric_dtype(series):
            stats["Mean"].append(au_mean(series))
            stats["Std"].append(au_std(series))
            stats["Min"].append(au_min(series))
            stats["25%"].append(au_25(series))
            stats["50%"].append(au_50(series))
            stats["75%"].append(au_75(series))
            stats["Max"].append(au_max(series))
        else:
            stats["Mean"].append(None)
            stats["Std"].append(None)
            stats["Min"].append(None)
            stats["25%"].append(None)
            stats["50%"].append(None)
            stats["75%"].append(None)
            stats["Max"].append(None)

# Création du DataFrame avec les statistiques comme lignes et les colonnes des
# données comme colonnes
summary_df = pd.DataFrame(stats, index=columns).T

# Affichage
print(summary_df)
