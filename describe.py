import pandas as pd
import math

df = pd.read_csv('./datasets/dataset_test.csv')

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


def au_mean(a):
    ret = 0
    for i in a:
        if not math.isnan(i):
            ret += i
    return ret / len(a)


def au_sum(a):
    ret = 0
    for i in a:
        if not math.isnan(i):
            ret += i
    return ret


def au_max(a):
    ret = -100000000
    for i in a:
        if not math.isnan(i):
            if i > ret:
                ret = i
    return ret


def au_min(a):
    ret = 100000000
    for i in a:
        if not math.isnan(i):
            if i < ret:
                ret = i
    return ret


def au_count(a):
    ret = 0
    for i in a:
        if not math.isnan(i):
            ret += 1
    return ret


def au_std(a):
    N = au_count(a)
    mean = au_mean(a)
    for i in a:
        if not math.isnan(i):
            d2 = abs(i - mean)**2
    return (d2.sum() / (N)) ** 0.5


columns = []  # Liste des noms des colonnes retenues

# Itération sur les colonnes
for series_name, series in df.items():
    if series_name not in ["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand"]:
        columns.append(series_name)  # Ajouter le nom de la colonne

        stats["count"].append(series.count())

        if pd.api.types.is_numeric_dtype(series):
            stats["Mean"].append(au_mean(series))
            stats["Std"].append(series.std())
            stats["Min"].append(series.min())
            stats["25%"].append(series.quantile(0.25))
            stats["50%"].append(series.median())
            stats["75%"].append(series.quantile(0.75))
            stats["Max"].append(series.max())
        else:
            stats["Mean"].append(None)
            stats["Std"].append(None)
            stats["Min"].append(None)
            stats["25%"].append(None)
            stats["50%"].append(None)
            stats["75%"].append(None)
            stats["Max"].append(None)

# Création du DataFrame avec les statistiques comme lignes et les colonnes des données comme colonnes
summary_df = pd.DataFrame(stats, index=columns).T

# Affichage
print(summary_df)
