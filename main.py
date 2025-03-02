import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o CSV com encoding adequado
df = pd.read_csv("Mobiles Dataset.csv", encoding="ISO-8859-1")

# Exibir as primeiras linhas para entender os dados
print(df.head())

# Ajuste: Ordenar os valores por preço
df_sorted = df.sort_values(by="Launched Price (USA)", ascending=False)

# Criar gráfico de barras vertical
plt.figure(figsize=(12, 6))
sns.barplot(x=df_sorted['Company Name'], y=df_sorted['Launched Price (USA)'])

# Melhorar a visualização
plt.xticks(rotation=90)  # Rotacionar rótulos para evitar sobreposição
plt.title("Preço de Lançamento por Marca")
plt.xlabel("Marcas")
plt.ylabel("Preço (USD)")
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Adicionar linhas de grade para melhor leitura

# Mostrar o gráfico
plt.show()
