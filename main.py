import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Mobiles Dataset.csv", encoding="ISO-8859-1")


print(df.head())


df_sorted = df.sort_values(by="Launched Price (USA)", ascending=False)

 
plt.figure(figsize=(12, 6))
sns.barplot(x=df_sorted['Company Name'], y=df_sorted['Launched Price (USA)'])


plt.xticks(rotation=90)  
plt.title("Preço de Lançamento por Marca")
plt.xlabel("Marcas")
plt.ylabel("Preço (USD)")
plt.grid(axis="y", linestyle="--", alpha=0.7)  


plt.show()