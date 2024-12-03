import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset
file_path = "amazon.csv"  # Cambia por la ruta de tu archivo
df = pd.read_csv(file_path)

# Vista inicial de los datos
print("Primeras filas del dataset:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

# Revisar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Distribución de calificaciones
plt.figure(figsize=(8, 5))
sns.countplot(x="rating", data=df, palette="viridis")
plt.title("Distribución de las calificaciones")
plt.xlabel("Calificación")
plt.ylabel("Frecuencia")
plt.show()

# Longitud de los títulos y su relación con las calificaciones
df["title_length"] = df["title"].apply(lambda x: len(str(x)))

plt.figure(figsize=(8, 5))
sns.boxplot(x="rating", y="title_length", data=df, palette="coolwarm")
plt.title("Relación entre la longitud del título y la calificación")
plt.xlabel("Calificación")
plt.ylabel("Longitud del título")
plt.show()
