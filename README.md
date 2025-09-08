# 🏡 Proyecto de Limpieza de Datos de Airbnb

Este proyecto consiste en la limpieza y preparación de un dataset de **Airbnb** para análisis de datos.  
El objetivo es transformar la base cruda en un dataset estructurado y listo para análisis estadístico o modelos de machine learning.

---

## 📂 Dataset
El dataset original proviene de: **Airbnb Open Data** de **Kaggle**.  
Archivo utilizado: `Airbnb_Open_Data.csv`.

---

## 🛠️ Pasos realizados

1. **Importación de datos** usando `pandas`.  
2. **Selección de columnas relevantes** y eliminación de las innecesarias.  
3. **Revisión y eliminación de duplicados**.  
4. **Tratamiento de valores faltantes (NA)**:
   - Eliminación de la columna `last review` por exceso de datos nulos.
   - Eliminación de filas con valores faltantes.  
5. **Transformaciones adicionales**:
   - Conversión de la columna `price` a formato numérico.  
   - Reset del índice para mantener consistencia.  
6. **Exportación del dataset limpio** a `Airbnb_Limpio.csv`.

---

## 📊 Resultados

- Dataset original: **X columnas y Y filas**  
- Dataset limpio: **X columnas y Y filas** (ajusta con tus valores reales).  
- Archivo final: `Airbnb_Limpio.csv`.

---

## 💻 Tecnologías utilizadas
- Python 3  
- Pandas  

---

## 🚀 Próximos pasos
- Realizar un **análisis exploratorio de datos (EDA)**.  
- Visualizar tendencias (precios, tipos de alojamiento, barrios, etc.).  
- Preparar dataset para **modelos predictivos** (ej. predicción de precio).  

---

## 📌 Autor
Proyecto realizado por *AnVales* como práctica de **Análisis de Datos**.
