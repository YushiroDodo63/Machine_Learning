# # coding: utf-8
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 教師データと刑法リストの読み込み
df = pd.read_csv("./dataset.csv", encoding="shift_jis")
print(df.columns)
print(pd.isna(df["Age"]))
