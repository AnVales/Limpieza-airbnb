import pandas as pd

#Importación de datos
data = pd.read_csv(r"C:\Users\yayau\Downloads\airbnb\Airbnb_Open_Data.csv")  
 
print(data.head())
print(data.info())
print(data.columns)

# Eliminación de columnas innecesarias
eliminar = ['reviews per month', 'review rate number', 'calculated host listings count', 'availability 365', 'house_rules', 'license', 'id']
keep = ['NAME', 'host id', 'host_identity_verified', 'host name', 'neighbourhood group', 'neighbourhood', 'lat', 'long', 'country', 'country code', 
        'instant_bookable', 'cancellation_policy', 'room type', 'Construction year', 'price', 'service fee', 'minimum nights', 'number of reviews', 
        'last review']

# Filtrado de columnas
print(f"Columnas antes de eliminar: {data.shape[1]}")
data_1 = data[keep].copy()
print(f"Columnas después de eliminar: {data_1.shape[1]}")

# revisión
print(data_1.columns)

# renombrar columnas
data_1.rename(columns = {"NAME": "Name"}, inplace = True)

# mirar valores duplicados
print(f"Valores duplicados: {data_1.duplicated().sum()}")

# quitar duplicados
data_1.drop_duplicates(inplace = True)

# mirar valores duplicados AHORA
print(f"Valores duplicados: {data_1.duplicated().sum()}")

# revisar valores NA
print(f"Valores NA: {data_1.isna().sum()}")

# eliminar la columna 'last review' por tener muchos NA
data_1.drop(columns = ['last review'], inplace = True)

# eliminar filas con NA
data_1.dropna(inplace = True)

# revisar valores NA nuevamente
print(f"Valores NA: {data_1.isna().sum()}")

# cambiar el index
data_1.reset_index(drop = True, inplace = True)

# poder datos object a numeric
data_1['price'] = data_1['price'].str.replace('$', '').str.replace(',', '').astype(float)

# guardar el dataframe limpio
data_1.to_csv(r"C:\Users\yayau\Downloads\airbnb\Airbnb_Limpio.csv", index = False)  