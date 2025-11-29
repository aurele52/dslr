from pandas.core.describe import pd
import matplotlib.pyplot as plt

palette = {
    "Gryffindor": "tab:red",
    "Slytherin":  "tab:green",
    "Ravenclaw":  "tab:blue",
    "Hufflepuff": "tab:orange",
}


def scatter(name1, name2):
    df = pd.read_csv('./datasets/dataset_train.csv')
    df = df[[name1, name2, "Hogwarts House"]].copy()
    print(df)
    plt.figure(figsize=(7, 4.5))
    plt.scatter(df[name1], df[name2], s=30, alpha=0.75,
                c=df["Hogwarts House"].map(palette))
    plt.title("Nuage de points " + name1 + " / " + name2)
    plt.xlabel(name1)
    plt.ylabel(name2)
    plt.grid(True, linewidth=0.5, alpha=0.5)
    plt.show()


# scatter("Astronomy", "Defense Against the Dark Arts")
# scatter("Ancient Runes", "History of Magic")
scatter("Astronomy", "Herbology")
