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