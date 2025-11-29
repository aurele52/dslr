import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

palette = {
    "Gryffindor": "tab:red",
    "Slytherin":  "tab:green",
    "Ravenclaw":  "tab:blue",
    "Hufflepuff": "tab:orange",
}


def pair_plot(names):
    df = pd.read_csv('./datasets/dataset_train.csv')
    names = names + ["Hogwarts House"]
    d = df[names].dropna()
    scatter_matrix(d, figsize=(20, 20), diagonal="hist",
                   alpha=0.6, s=12, c=d["Hogwarts House"].map(palette))
    plt.suptitle("Scatter matrix", y=1.02)
    plt.tight_layout()
    plt.show()


pair_plot(["Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies",
          "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"])
