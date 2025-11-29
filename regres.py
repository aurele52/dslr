
import math
import pandas as pd

df = pd.read_csv('./datasets/dataset_train.csv')
df = df.drop(columns=["Index", "First Name",
             "Last Name", "Birthday", "Best Hand"])
print(df)

taux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
learning_rate = 0.00000000000001


def sygmoide(value):
    return 1 / (1 + math.exp(-value))


def hypothese(value):
    hypo = 0
    for index, val in value:
        if isinstance(val, (int, float)):
            hypo = hypo + val * taux[index]
    return sygmoide(hypo)


def loss(house):
    nombre_eleve = len(df)
    somme = 0
    print(nombre_eleve)
    for index, value in df.iterrows():
        isIn = value["Hogwarts House"] == house
        print(isIn)
        test = isIn * math.log(hypothese(value)) + \
            (1 - isIn) * math.log(1 - hypothese(value))
        print(test)
        somme = somme + test
        print(value)
    fiabiliter = -(somme / nombre_eleve)
    return fiabiliter
    print(nombre_eleve)


def gradient(house, index_cour):
    somme = 0
    nombre_eleve = len(df)
    for index, value in df.iterrows():
        isIn = value["Hogwarts House"] == house
        test = (hypothese(value) - isIn) * taux[index_cour]
        somme = somme + test
    res = somme / nombre_eleve
    return res


def descent_gradient(house):
    index = 0
    for index, val in df:
        taux[index] = taux[index] - learning_rate * gradient(house, index)


loss("Hufflepuff")
