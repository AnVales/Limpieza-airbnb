import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Importación de datos
data = pd.read_csv(r"C:\Users\yayau\Downloads\airbnb\Airbnb_Limpio.csv")  

# Diccionario de traducción
labels_dict = {
    "Entire home/apt": "Departamento completo",
    "Private room": "Habitación privada",
    "Shared room": "Habitación compartida",
    "Hotel room": "Habitación de hotel"
}

# Distribución de precios
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.histplot(
    x=data['price'],
    hue=data['room type'],
    multiple="stack",   # <<--- evita superposición
    palette="Set2"
)
plt.title('Distribución de Precios de Airbnb por Tipo de Habitación')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.xlim(45, 1330)  # Limitar el eje x para mejor visualización
plt.xticks([50, 250, 450, 650, 850, 1050])
plt.show()

# Precio promedio por barrio
sns.barplot(x='neighbourhood group', y='price', data=data, errorbar=None, palette="Set2", order=data.groupby('neighbourhood group')['price'].mean().sort_values().index)
plt.xticks(rotation=45)
plt.title("Precio promedio por barrio")
plt.xlabel(' ')
plt.ylabel('Precio')
plt.show()

# Correlación entre precio y número de reviews
# plt.scatter(x='price', y='number of reviews', data=data, alpha= 0.8)
plt.scatter(x=data['price'], y=data['number of reviews'], alpha=0.5)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Precio')
plt.ylabel('Número de Reviews')
plt.show()

# Correlación de la verificación del anfitrión y el precio
# sns.barplot(x='price', y='host_identity_verified', data=data, errorbar=None, palette="Set2")
sns.boxplot(x='host_identity_verified', y='price', data=data, palette="Set2")
plt.xticks(rotation=45)
plt.xlabel('Verificación del Anfitrión')
plt.ylabel('Precio')
plt.show()

# Correlación entre precio y tipo de habitación
plt.scatter(x='price', y='room type', data=data, alpha= 0.8)
plt.xlabel('Precio')
plt.ylabel(' ')
plt.show()

# Correlación entre precio y política de cancelación
sns.violinplot(x='cancellation_policy', y='price', data=data, palette="Set2")
plt.xlabel('Política de Cancelación')
plt.ylabel('Precio')
plt.title('Precio según política de cancelación')
plt.show()

# Mapa de calor de correlación numérica
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", center=0)
plt.show()

# Mapa geográfico de precios
sns.scatterplot(x='long', y='lat', hue='price', size='price', data=data, palette="viridis", alpha=0.6, legend=False)
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title("Mapa de precios Airbnb")
plt.legend(title='Precio', loc='upper right')
plt.show()

# Outliers
from scipy.stats import zscore

# Calculate z-score for each data point and compute its absolute value
z_scores = zscore(data['price'])
abs_z_scores = np.abs(z_scores)

# Select the outliers using a threshold of 3
outliers = data[abs_z_scores > 3]
print(outliers.head())

# Import MAD estimator
from pyod.models.mad import MAD

# Set threshold to 3.5
mad = MAD(threshold = 3.5)

# Convert the 'total' column into a 2D numpy array
total_reshaped = data['price'].values.reshape(-1, 1)

# Generate inline and outlier labels
labels = mad.fit(total_reshaped).labels_
print(labels)

# Obtain number of outliers
print(f'Number of outliers: {labels.sum()}')

outliers = data[labels == 1]
print(outliers.head())

# Visualización de outliers con boxplot
sns.boxplot(x='room type', y='price', data=data)
plt.title('Detección de Outliers en Precios por Tipo de Habitación')
plt.ylabel('Precio')
plt.show()

# Visualización de outliers con catqplot
sns.catplot(x="neighbourhood group", y="price", hue="room type", data=data, kind="bar", height=6, aspect=2)
plt.title('Precio Promedio por Barrio y Tipo de Habitación')
plt.ylabel('Precio')
plt.xlabel('Barrio')
plt.show()
