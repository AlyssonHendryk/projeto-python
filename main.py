import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregar o CSV com encoding adequado
df = pd.read_csv("Mobiles Dataset.csv", encoding="ISO-8859-1")

# Filtrar apenas as marcas desejadas
df = df[df["Company Name"].isin(["Motorola", "Apple", "Samsung"])]

# Limpar e converter a coluna "Screen Size"
df["Screen Size"] = df["Screen Size"].astype(str)  # Converter para string para tratamento
df["Screen Size"] = df["Screen Size"].str.extract(r"(\d+\.\d+)")  # Pega apenas o número antes de "inches"
df["Screen Size"] = pd.to_numeric(df["Screen Size"], errors="coerce")  # Converter para float

#Filtrar o intervalo desejado (6.0 a 6.9) e arredondar
df = df[(df["Screen Size"] >= 6.0) & (df["Screen Size"] <= 6.9)]
df["Screen Size"] = df["Screen Size"].round(1)  # Arredondar para 1 casa decimal

#Limpar a coluna de RAM (Pegar apenas o primeiro valor e remover "GB")
df["RAM"] = df["RAM"].str.split(" / ").str[0]  # Se houver mais de um valor, pegar o primeiro
df["RAM"] = df["RAM"].str.replace("GB", "", regex=True)
df["RAM"] = pd.to_numeric(df["RAM"], errors="coerce")

#Converter colunas numéricas
df["Launched Year"] = pd.to_numeric(df["Launched Year"], errors="coerce")

# Gráfico de Distribuição do Tamanho de Tela (Com cores alteradas)
plt.figure(figsize=(10, 5))
ax = sns.countplot(y=df["Screen Size"], order=sorted(df["Screen Size"].unique()), palette="coolwarm")

# Adicionar porcentagens nas barras
total = len(df)
for p in ax.patches:
    percentage = f'{100 * p.get_width() / total:.1f}%'
    ax.annotate(percentage, (p.get_width() + 0.5, p.get_y() + 0.4), ha='center', va='center')

plt.title("Distribuição dos Tamanhos de Tela (6.0 - 6.9 polegadas)")
plt.xlabel("Quantidade de Celulares")
plt.ylabel("Tamanho da Tela (polegadas)")
plt.show()

# Gráfico de Distribuição da RAM por Marca - Barras Agrupadas
plt.figure(figsize=(10, 5))
ax = sns.countplot(data=df, x="RAM", hue="Company Name", palette={"Motorola": "blue", "Apple": "red", "Samsung": "yellow"})

# Adicionar porcentagens nas barras
total = len(df)
for p in ax.patches:
    height = p.get_height()
    if height > 0:  
        percentage = f'{100 * height / total:.1f}%'
        ax.annotate(percentage, (p.get_x() + p.get_width() / 2, height), ha='center', va='bottom')

plt.title("Distribuição da Memória RAM por Marca (Barras Agrupadas)")
plt.xlabel("Memória RAM (GB)")
plt.ylabel("Quantidade de Celulares")
plt.legend(title="Marca")
plt.show()

# Gráfico de Celulares Lançados ao Longo do Tempo por Marca (Barras Agrupadas)
plt.figure(figsize=(12, 6))
ax = sns.countplot(data=df, x="Launched Year", hue="Company Name", palette={"Motorola": "blue", "Apple": "red", "Samsung": "yellow"})

# Adicionar porcentagens sobre as barras
total = len(df)
for p in ax.patches:
    height = p.get_height()
    if height > 0:  
        percentage = f'{100 * height / total:.1f}%'
        ax.annotate(percentage, (p.get_x() + p.get_width() / 2, height), ha='center', va='bottom')

plt.title("Quantidade de Celulares Lançados por Marca ao Longo do Tempo")
plt.xlabel("Ano de Lançamento")
plt.ylabel("Quantidade de Celulares")
plt.xticks(rotation=45)
plt.legend(title="Marca")
plt.show()