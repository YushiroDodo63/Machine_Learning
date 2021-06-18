# # coding: utf-8
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.preprocessing as sp

df = pd.read_csv("./dataset.csv", encoding="shift_jis")

le = sp.LabelEncoder()
le.fit(df.Sex.unique())
df.Sex = le.fit_transform(df.Sex)
sns.pairplot(df, hue='Survived')
