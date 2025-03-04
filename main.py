import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

tabela_df = pd.read_csv("Mobiles Dataset.csv", encoding="ISO-8859-1", sep=",")

modelo_df = tabela_df.loc[tabela_df['Model'] != 'Name']