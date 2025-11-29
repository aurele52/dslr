import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/dataset_train.csv')

print(df)
df = df.drop(columns=["Index", "Hogwarts House", "First Name", "Last Name",
                      "Birthday", "Best Hand"])
print(df)
color = ['green', 'blue', 'red', 'cyan', 'magenta', 'yellow', 'black',
         'darkgreen', 'orange', 'blueviolet', 'darkred', 'olive', 'chocolate']


i = 0
for series_name, series in df.items():
    if series_name not in ["Index", "Hogwarts House", "First Name",
                           "Last Name", "Birthday", "Best Hand"]:
        df[series_name] = (df[series_name] - df[series_name].min()) / \
            (df[series_name].max() - df[series_name].min())
        plt.hist(df[series_name], bins=30, alpha=0.5,
                 color=color[i], label=str(series_name))
        i += 1

print(df)
# # data = pd.DataFrame({
# #     'Feature 1': np.random.normal(loc=1, scale=1, size=1000),
# #     'Feature 2': np.random.normal(loc=0, scale=1, size=1000),
# #     'Feature 3': np.random.normal(loc=-1, scale=1, size=1000)
# # })
#
# plt.figure(figsize=(8, 6))
# plt.hist(data['Feature 2'], bins=30, alpha=0.5, color='green', label='Feature 2')
# plt.hist(data['Feature 3'], bins=30, alpha=0.5, color='red', label='Feature 3')
#
# # Personnalisation
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.legend()
plt.show()
